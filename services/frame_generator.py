# backend/services/frame_generator.py

from PIL import Image, ImageDraw, ImageFont
import os


OUTPUT_FRAME_FOLDER = "output/frames"


def generate_frame(scene_text: str, code_text: str, file_name: str):
    """
    Create a tutorial frame image for one scene

    Example:
    scene_text = "Here is a simple for loop example"
    code_text = "for i in range(5):\n    print(i)"
    file_name = "frame_1.png"

    Output:
    output/frames/frame_1.png
    """

    # create folder if it doesn't exist
    os.makedirs(OUTPUT_FRAME_FOLDER, exist_ok=True)

    file_path = os.path.join(OUTPUT_FRAME_FOLDER, file_name)

    # create dark background image
    img = Image.new("RGB", (1280, 720), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)

    # default font
    font = ImageFont.load_default()

    # title / explanation text
    draw.text((50, 50), scene_text, fill=(255, 255, 255), font=font)

    # code section
    if code_text:
        draw.text((50, 150), code_text, fill=(100, 200, 255), font=font)

    # save image
    img.save(file_path)

    return file_path