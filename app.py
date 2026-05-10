# backend/app.py

from fastapi import FastAPI
from pydantic import BaseModel

from services.ollama_service import generate_tutorial_script
from services.scene_builder import build_scenes
from services.tts_service import generate_audio
from services.frame_generator import generate_frame
from services.video_builder import build_final_video


app = FastAPI(title="AI CodeTutor Video Generator")


class VideoRequest(BaseModel):
    topic: str


@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "Backend is working"
    }


@app.get("/generate-video")
def generate_video(request: VideoRequest):
    """
    Full pipeline:

    topic
      ↓
    Ollama → script
      ↓
    Scene Builder → scenes
      ↓
    TTS → audio files
      ↓
    Frame Generator → image frames
      ↓
    Video Builder → final video
      ↓
    Return final response
    """

    topic = request.topic

    # Step 1: Generate tutorial script using Ollama
    script = generate_tutorial_script(topic)

    # Step 2: Convert script into structured scenes
    scenes = build_scenes(script)

    frame_paths = []
    audio_paths = []

    # Step 3 + 4: Generate audio + frames for each scene
    for index, scene in enumerate(scenes, start=1):
        scene_text = scene["text"]
        code_text = scene["code"]

        audio_path = generate_audio(
            scene_text=scene_text,
            file_name=f"audio_{index}.mp3"
        )

        frame_path = generate_frame(
            scene_text=scene_text,
            code_text=code_text,
            file_name=f"frame_{index}.png"
        )

        audio_paths.append(audio_path)
        frame_paths.append(frame_path)

    # Step 5: Build final video
    final_video_path = build_final_video(
        frame_paths=frame_paths,
        audio_paths=audio_paths
    )

    return {
        "topic": topic,
        "generated_script": script,
        "scenes": scenes,
        "final_video": final_video_path
    }