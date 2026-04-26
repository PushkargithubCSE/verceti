# backend/services/tts_service.py

from gtts import gTTS
import os


OUTPUT_AUDIO_FOLDER = "output/audio"


def generate_audio(scene_text: str, file_name: str):
    """
    Convert scene text into audio using gTTS

    Example:
    scene_text = "A for loop repeats actions"
    file_name = "audio_1.mp3"

    Output:
    output/audio/audio_1.mp3
    """

    # create folder if it doesn't exist
    os.makedirs(OUTPUT_AUDIO_FOLDER, exist_ok=True)

    file_path = os.path.join(OUTPUT_AUDIO_FOLDER, file_name)

    try:
        tts = gTTS(text=scene_text, lang="en")
        tts.save(file_path)

        return file_path

    except Exception as e:
        return f"TTS generation error: {str(e)}"