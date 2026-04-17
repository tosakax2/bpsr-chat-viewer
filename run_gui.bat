@echo off
setlocal enabledelayedexpansion

cd /d %~dp0

REM --- Admin Rights Check ---
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Administrative privileges required. Requesting elevation...
    powershell -Command "Start-Process -FilePath '%0' -Verb RunAs"
    exit /b
)

echo ========================================================
echo        BPSR Chat Viewer - Standalone GUI
echo ========================================================

REM --- Update Frontend Build ---
echo [INFO] Updating frontend build...
cd frontend
if not exist "node_modules" (
    echo [INFO] Installing frontend dependencies...
    call npm install --legacy-peer-deps
)
echo [INFO] Building chat interface...
call npm run build
cd ..

echo [INFO] Starting Backend GUI...
cd backend

REM Ensure virtual environment exists
if not exist .venv (
    echo [INFO] Creating virtual environment...
    uv venv --seed
)

REM Sync dependencies
echo [INFO] Syncing dependencies...
uv sync --quiet

REM Launch the app
echo [INFO] App is launching in a new window. You can minimize this CLI.
start .venv\Scripts\pythonw.exe main.py
exit
