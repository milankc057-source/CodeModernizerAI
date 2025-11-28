import subprocess
import webbrowser
import time
import os

# Change directory to your backend folder
os.chdir(r"C:\Users\DELL\OneDrive\Desktop\CodeModernizerAI\backend")

# Start FastAPI server in the background (no window)
subprocess.Popen(
    ["python", "-m", "uvicorn", "main:app", "--reload"],
    creationflags=subprocess.CREATE_NO_WINDOW
)

# Wait a few seconds for server to start
time.sleep(5)

# Open FastAPI docs in default browser
webbrowser.open("http://127.0.0.1:8000/docs")
