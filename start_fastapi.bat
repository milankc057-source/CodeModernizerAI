@echo off
cd "C:\Users\DELL\OneDrive\Desktop\CodeModernizerAI\backend"

REM Start FastAPI server
start python -m uvicorn main:app --reload

REM Wait a few seconds for server to start
timeout /t 5

REM Open browser automatically
start http://127.0.0.1:8000/docs
