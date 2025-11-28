from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os
from ai_engine import process_project

app = FastAPI()

PROJECTS_DIR = "uploaded_projects"
MODERNIZED_DIR = "modernized_projects"

# Ensure directories exist
os.makedirs(PROJECTS_DIR, exist_ok=True)
os.makedirs(MODERNIZED_DIR, exist_ok=True)

@app.post("/projects/upload")
async def upload_project(
    file: UploadFile = File(...),
    modernization_level: str = Form("light")
):
    project_name, _ = os.path.splitext(file.filename)
    uploaded_path = os.path.join(PROJECTS_DIR, f"{project_name}.txt")

    # Save uploaded file
    with open(uploaded_path, "wb") as f:
        f.write(await file.read())

    # Try real AI modernization first
    try:
        process_project(project_name, level=modernization_level, use_mock=False)
    except Exception as e:
        # If OpenAI fails, fallback to mock
        print(f"[WARNING] OpenAI modernization failed: {e}")
        process_project(project_name, level=modernization_level, use_mock=True)

    return JSONResponse(
        {"message": f"Project '{project_name}' uploaded and modernized with level '{modernization_level}'"}
    )
