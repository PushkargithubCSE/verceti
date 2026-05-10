# backend/services/scene_builder.py

def build_scenes(script: str):
    """
    Convert raw Ollama script into structured scenes
    for video generation.

    Example Input:

    1. A for loop repeats actions
    2. It helps avoid repeated code
    3. Example:
    for i in range(5):
        print(i)
    4. This prints numbers from 0 to 4

    Example Output:

    [
        {
            "text": "A for loop repeats actions",
            "code": ""
        },
        {
            "text": "Here is the code example",
            "code": "for i in range(5):\nprint(i)"
        }
    ]
    """

    lines = script.split("\n")

    scenes = []
    code_lines = []

    for line in lines:
        clean_line = line.strip()

        if not clean_line:
            continue

        # detect code lines
        if "for " in clean_line or "print(" in clean_line:
            code_lines.append(clean_line)
            continue

        # normal explanation text
        scenes.append({
            "text": clean_line,
            "code": ""
        })

    # add code scene separately
    if code_lines:
        scenes.append({
            "text": "Here is the code example",
            "code": "\n".join(code_lines)
        })

    return scenes