@echo off
setlocal

cd /d %~dp0

echo ========================================================
echo        BPSR Chat Viewer - EXE Builder (onedir)
echo ========================================================

echo [INFO] Building Frontend...
cd frontend
if not exist "node_modules" (
    echo [INFO] Installing frontend dependencies...
    call npm install --legacy-peer-deps
)
call npm run build
cd ..\backend

echo [INFO] Ensuring PyInstaller is available in Backend...
call uv add pyinstaller

echo [INFO] Creating Executable...
REM --windowed Hides console
REM --uac-admin Requests elevation on EXE startup
REM --add-data Includes frontend dist
call uv run pyinstaller --noconfirm --name BPSRChatViewer --windowed --uac-admin --paths star_resonance_relay/proto --add-data "../frontend/dist;frontend/dist" main.py

echo ========================================================
echo [INFO] Build Complete! 
echo [INFO] Executable folder: backend\dist\BPSRChatViewer
echo [INFO] Please run BPSRChatViewer.exe from that folder.
echo ========================================================
pause
