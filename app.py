# backend/app.py

from fastapi import FastAPI
from pydantic import BaseModel

from services.ollama_service import generate_tutorial_script

app = FastAPI(title="AI CodeTutor Video Generator")


class VideoRequest(BaseModel):
    topic: str


@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "Backend is working"
    }


@app.post("/generate-video")
def generate_video(request: VideoRequest):
    """
    Step 1:
    Receive topic from frontend

    Example:
    {
        "topic": "Teach me Python for loops"
    }

    Step 2:
    Send topic to Ollama

    Step 3:
    Return generated script
    (Later we will add TTS + Frames + Final Video)
    """

    script = generate_tutorial_script(request.topic)

    return {
        "topic": request.topic,
        "generated_script": script
    }