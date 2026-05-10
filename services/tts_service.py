# backend/services/tts_service.py

import pyttsx3
import os


OUTPUT_AUDIO_FOLDER = "output/audio"


def generate_audio(scene_text: str, file_name: str):

    os.makedirs(OUTPUT_AUDIO_FOLDER, exist_ok=True)

    file_path = os.path.join(OUTPUT_AUDIO_FOLDER, file_name)

    try:
        engine = pyttsx3.init()

        engine.save_to_file(scene_text, file_path)
        engine.runAndWait()

        return file_path

    except Exception as e:
        return f"TTS generation error: {str(e)}"