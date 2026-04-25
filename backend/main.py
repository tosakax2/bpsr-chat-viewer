import asyncio
import logging
import json
import threading
import contextlib
import webview
import os
import sys

# Redirect stdout/stderr to a log file when running via pythonw.exe (which sets them to None)
if sys.stdout is None or sys.stderr is None:
    try:
        log_path = os.path.join(os.path.dirname(__file__), "app.log")
        log_file = open(log_path, "a", encoding="utf-8")
        sys.stdout = log_file
        sys.stderr = log_file
    except Exception:
        pass

from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from google.protobuf.message import Message

from star_resonance_relay.sniffer import BPSRChatSniffer
from star_resonance_relay.processor import BPSRPacketProcessor
from star_resonance_relay.proto.serv_chit_chat_ntf_pb2 import ChitChatNtf
from star_resonance_relay.proto.stru_notify_newest_chit_chat_msgs_request_pb2 import NotifyNewestChitChatMsgsRequest
from star_resonance_relay.proto.enum_chit_chat_channel_type_pb2 import ChitChatChannelType
from star_resonance_relay.proto.enum_chit_chat_msg_type_pb2 import ChitChatMsgType
from scapy.sendrecv import sniff

# Global event loop for thread-safe broadcasting
main_loop = None

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    global main_loop
    main_loop = asyncio.get_running_loop()
    # Start sniffing in a separate thread
    thread = threading.Thread(target=start_sniffing, daemon=True)
    thread.start()
    yield

app = FastAPI(lifespan=lifespan)

# Enable CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        try:
            self.active_connections.remove(websocket)
        except ValueError:
            pass

    async def broadcast(self, message: dict):
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception:
                disconnected.append(connection)
        
        for conn in disconnected:
            try:
                self.active_connections.remove(conn)
            except ValueError:
                pass

manager = ConnectionManager()

# Map protobuf channel types to strings for the frontend
CHANNEL_MAPPING = {
    ChitChatChannelType.ChannelWorld: "world",
    ChitChatChannelType.ChannelScene: "scene",
    ChitChatChannelType.ChannelUnion: "guild",
    ChitChatChannelType.ChannelTeam: "party",
    ChitChatChannelType.ChannelSystem: "system",
}

def on_bpsr_message(payload: Message):
    if not isinstance(payload, ChitChatNtf.NotifyNewestChitChatMsgs):
        return

    req: NotifyNewestChitChatMsgsRequest = payload.v_request
    channel_key = CHANNEL_MAPPING.get(req.channel_type)
    
    if not channel_key:
        return

    # Extract message info
    msg_info = req.chat_msg.msg_info
    content = ""
    
    if msg_info.msg_type == ChitChatMsgType.ChatMsgTextMessage:
        content = msg_info.msg_text
    elif msg_info.msg_type == ChitChatMsgType.ChatMsgPictureEmoji:
        content = f"[Emoji: {msg_info.picture_emoji.config_id}]"
    elif msg_info.msg_type == ChitChatMsgType.ChatMsgHypertext:
        content = "[Hypertext Content]"
    
    chat_data = {
        "channel": channel_key,
        "sender": req.chat_msg.send_char_info.name,
        "content": content,
        "timestamp": req.chat_msg.timestamp
    }
    
    logger.debug(f"Broadcast: {chat_data}")
    
    # Broadcast to all connected clients
    if main_loop:
        try:
            if main_loop.is_running():
                asyncio.run_coroutine_threadsafe(manager.broadcast(chat_data), main_loop)
            else:
                logger.warning("Main event loop is not running")
        except Exception as e:
            logger.error(f"Error broadcasting message: {e}")
    else:
        logger.warning("Main event loop is not initialized")

def start_sniffing():
    """Two-phase packet sniffer to minimise Npcap driver contention.

    Phase 1 – Discovery:
        Uses a broad 'tcp' BPF filter for only as long as it takes to find
        the game server's IP address (typically a few seconds at startup or
        after a scene change).  scapy stops the capture the moment the server
        signature is detected.

    Phase 2 – Locked:
        Restarts scapy with a precise 'tcp and host <ip>' filter.  The Npcap
        driver evaluates this filter *in-kernel* before any data reaches
        Python, so the application sees only game-server packets.  This
        eliminates almost all contention with other Npcap-based tools such as
        DPS checkers.

        Phase 2 runs for PHASE2_TIMEOUT seconds before cycling back to
        Phase 1, so that a server IP change after a scene transition is
        eventually detected.
    """
    import time

    # How long (seconds) to stay in Phase 2 before re-running discovery.
    # Shorter = faster reconnect after scene change; longer = less overhead.
    PHASE2_TIMEOUT = 60

    logger.info("Starting packet sniffer (two-phase mode)...")
    sniffer = BPSRChatSniffer(on_bpsr_message)

    while True:
        # ── Phase 1: broad discovery ──────────────────────────────────────
        if sniffer._known_server is None:
            logger.info("Sniffer Phase 1: broad discovery (filter='tcp')")
            sniff(
                filter="tcp",
                prn=sniffer.handle_packet,
                store=False,
                # stop_filter runs on the capture thread – safe because
                # handle_packet also runs there (no race).
                stop_filter=lambda _: sniffer._known_server is not None,
            )

        server = sniffer._known_server
        if server is None:
            # Interrupted before server was found; wait briefly and retry.
            time.sleep(0.5)
            continue

        # ── Phase 2: locked to server IP ─────────────────────────────────
        locked_ip = server.source.ip
        bpf = f"tcp and host {locked_ip}"
        logger.info(f"Sniffer Phase 2: locked (filter='{bpf}')")

        sniff(
            filter=bpf,
            prn=sniffer.handle_packet,
            store=False,
            timeout=PHASE2_TIMEOUT,
        )

        # After the timeout check whether the server IP is still the same.
        current = sniffer._known_server
        if current is None or current.source.ip != locked_ip:
            # Server IP changed (scene change to a different host) or
            # connection was lost – return to Phase 1 for rediscovery.
            logger.info("Sniffer: server IP changed or lost, restarting discovery.")
            sniffer._known_server = None
        else:
            # Same IP still active; simply restart Phase 2 without discovery.
            logger.info(f"Sniffer Phase 2: timeout, re-locking to {locked_ip}")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# Check for built frontend and mount static files
def get_resource_path(*paths):
    import sys
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, *paths)
    return os.path.join(os.path.dirname(__file__), "..", *paths)

dist_path = get_resource_path("frontend", "dist")
if os.path.exists(dist_path):
    logger.info(f"Serving built frontend from {dist_path}")
    app.mount("/", StaticFiles(directory=dist_path, html=True), name="static")
else:
    logger.warning("Built frontend not found. Fallback to dev server.")

class Api:
    def __init__(self):
        # Settings file is located in the same directory as the executable
        if getattr(sys, 'frozen', False):
            # If the application is run as a bundle (PyInstaller)
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            
        # If in dev, we might want it in the project root instead of backend folder
        if base_dir.endswith('backend'):
            base_dir = os.path.dirname(base_dir)
            
        self.settings_path = os.path.join(base_dir, "settings.json")

    def load_settings(self):
        try:
            if os.path.exists(self.settings_path):
                with open(self.settings_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Error loading settings: {e}")
        return {}

    def save_settings(self, settings_dict):
        try:
            with open(self.settings_path, 'w', encoding='utf-8') as f:
                json.dump(settings_dict, f, ensure_ascii=False, indent=4)
        except Exception as e:
            logger.error(f"Error saving settings: {e}")

    def open_popout(self, channel: str):
        logger.info(f"Opening native pop-out for channel: {channel}")
        
        # Determine base URL (match logic used for main window)
        current_dist_path = get_resource_path("frontend", "dist")
        if os.path.exists(current_dist_path):
            base_url = "http://localhost:8000"
        else:
            base_url = "http://localhost:5173"
            
        url = f"{base_url}/?channel={channel}"
        
        # Create a new standalone window for the specific channel
        webview.create_window(
            f"BPSR Chat - {channel.capitalize()}",
            url,
            width=450,
            height=700,
            min_size=(360, 480)
        )

def run_server():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="warning")

if __name__ == "__main__":
    # Start the backend server in a separate thread
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # Initialize JS-Python API
    api = Api()
    
    # Choose URL based on frontend availability
    if os.path.exists(dist_path):
        url = "http://localhost:8000"
    else:
        url = "http://localhost:5173"
        
    # Launch the standalone GUI window
    logger.info(f"Launching Standalone GUI pointing to {url}...")
    
    window = webview.create_window(
        "BPSR Chat Viewer", 
        url, 
        width=450, 
        height=800,
        min_size=(360, 480),
        js_api=api
    )
    
    def on_closed():
        logger.info("Main window closed. Exiting application...")
        import os
        os._exit(0)
        
    window.events.closed += on_closed
    
    # Store webview data (localStorage, cookies) in a dedicated folder in AppData
    app_data_dir = os.path.join(os.environ.get('APPDATA', ''), 'bpsr-chat-viewer')
    os.makedirs(app_data_dir, exist_ok=True)
    webview.start(private_mode=False, storage_path=app_data_dir)
