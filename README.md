# BPSR Chat Viewer

[**日本語版 / Japanese (README_ja.md)**](README_ja.md)

> [!WARNING]
> **Use at your own risk.** This project is an unofficial fan-made tool. It reads network traffic and is not affiliated with or endorsed by the developers or publishers of Star Resonance. By using this software, you assume all responsibility and risk for any potential consequences regarding your game account.

BPSR Chat Viewer is a standalone, professional-grade desktop application that captures and displays the in-game chat for **Star Resonance** in real-time. It provides an optimized, customizable GUI for better readability without modifying the game client.

## Features

* **Real-time Chat Sniffing**: Uses network capture to seamlessly fetch incoming chat messages.
* **Never Miss a Message**: Unlike the in-game chat interface, this application continues to display messages even during crafting screens, menus, or loading screens.
* **Unified Interface**: View messages across different channels (World, Guild, Channel, Team, System).
* **Channel Filtering**: Toggle visibility for specific channels to focus on the conversations you care about.
* **Pop-out Windows**: Open dedicated, standalone windows for specific channels.
* **Sound Notifications**: Distinct audio alerts for incoming messages with volume control.
* **Standalone Executable**: Distributed as an easy-to-use executable without manual environment setup.

## Download & Installation

The simplest way to use BPSR Chat Viewer is to download the pre-compiled executable.

### Step 1: Install Npcap (Required)
Because this application captures network traffic to read the game chat, it requires a system-level network driver.
1. Download **Npcap** from the [official website](https://npcap.com/#download).
2. Run the installer. The default installation options are perfectly fine.

### Step 2: Running the App
1. Go to the [Releases](../../releases) page of this repository.
2. Download the latest `.zip` release.
3. Extract the folder to your desired location.
4. Run `BPSRChatViewer.exe`.

> [!NOTE] 
> Windows will prompt you with a User Account Control (UAC) dialog requesting Administrator privileges upon launch. This is completely normal and required for the packet sniffer to function alongside Npcap.

## Building from Source

If you prefer to run the application from the source code or build the executable yourself, follow these steps:

### Prerequisites
* **Python** (via `uv` package manager)
* **Node.js** (for frontend)
* **Npm**
* **Npcap / WinPcap** (Required for `scapy` raw packet sniffing on Windows)

### 1. Running the Source Version
You can run the GUI directly using the provided batch file:
```bat
run_gui.bat
```
This script handles checking administrator privileges, installing/building the React frontend dependencies, creating the Python `.venv`, installing dependencies via `uv`, and launching the app.

### 2. Building the Executable
To package the app into a standalone `dist` folder:
```bat
build_exe.bat
```
Once the build completes, your application will be available at `backend/dist/BPSRChatViewer`. You can distribute this folder directly.

## Disclaimer
This project is an unofficial fan-made tool. It is not affiliated with, maintained, authorized, endorsed, or sponsored by the developers or publishers of Star Resonance. Use at your own risk.
