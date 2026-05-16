<div align="center">

# 🎬 AI CodeTutor Video Generator

### *Learn coding now with your own generated customized video tutorial *

<br>

<img src="https://img.shields.io/badge/Local%20LLM-Ollama-black?style=for-the-badge">
<img src="https://img.shields.io/badge/Backend-FastAPI-green?style=for-the-badge">
<img src="https://img.shields.io/badge/Video-MoviePy-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/TTS-Offline-orange?style=for-the-badge">

<br>
<br>

> Prompt in → Tutorial video out.

</div>

---

# ✨ What It Does

Input:

```text
Teach me Python for loops
```

Output:

✅ AI-generated tutorial script  
✅ Scene-by-scene lesson flow  
✅ Voice narration  
✅ Rendered coding frames  
✅ Final stitched tutorial video  

---

# 🧠 System Architecture

```text
User Prompt
    ↓
Ollama (TinyLlama)
    ↓
Scene Builder
    ↓
Offline TTS
    ↓
Frame Generator
    ↓
MoviePy Composer
    ↓
Final Video 🎬
```

---

# ⚡ Demo Pipeline

```text
"Teach me Python functions"

        ↓

Generate tutorial explanation

        ↓

Convert into structured scenes

        ↓

Generate narration audio

        ↓

Render coding frames

        ↓

Compose final tutorial video
```

---

# 🏗️ Tech Stack

## 🤖 AI

- **Ollama**
- **TinyLlama**

## ⚙️ Backend

- **Python**
- **FastAPI**

## 🎥 Video Generation

- **MoviePy**
- **Pillow (PIL)**

## 🔊 TTS

- **pyttsx3** (offline)

## 🌐 Frontend

- **HTML**
- **CSS**
- **JavaScript**

---

# 📂 Project Structure

```text
backend/
│
├── app.py
│
├── services/
│   ├── ollama_service.py
│   ├── scene_builder.py
│   ├── tts_service.py
│   ├── frame_generator.py
│   └── video_builder.py
│
├── output/
│   ├── audio/
│   ├── frames/
│   └── videos/
│
frontend/
│
├── index.html
├── style.css
└── script.js
```

---

# 🔥 How It Works

## 1️⃣ Script Generation

The user enters a coding topic.

Example:

```text
Teach me Python dictionaries
```

The backend sends the prompt to **Ollama**.

The local LLM generates:
- explanation
- tutorial flow
- code example

---

## 2️⃣ Scene Building

Raw LLM output is converted into structured scenes:

```json
{
  "text": "A dictionary stores key-value pairs",
  "code": "student = {'name': 'John'}"
}
```

This acts as the internal **video graph**.

---

## 3️⃣ Voice Generation

Each scene is converted into narration audio using offline TTS.

---

## 4️⃣ Frame Rendering

Each scene is rendered into:
- dark themed coding frames
- code blocks
- explanation overlays

---

## 5️⃣ Video Composition

MoviePy combines:
- rendered frames
- generated narration
- timing synchronization

into the final tutorial video.

---

# 🚀 Run Locally

## Clone Repo

```bash
git clone <YOUR_REPO_URL>
cd AI-CodeTutor-Video-Generator
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install FFmpeg

Verify installation:

```bash
ffmpeg -version
```

---

## Pull TinyLlama

```bash
ollama pull tinyllama
```

---

## Start Ollama

```bash
ollama run tinyllama
```

---

## Run Backend

```bash
cd backend
uvicorn app:app --reload
```

---

## Run Frontend

Open:

```text
frontend/index.html
```

---

# 🧪 Current Features

- ✅ Local LLM integration
- ✅ AI script generation
- ✅ Scene orchestration
- ✅ Offline narration generation
- ✅ Frame rendering
- ✅ Automated video composition

---

# 🚧 Future Improvements

- typing animations
- syntax highlighting
- subtitle generation
- better TTS models
- async rendering queue
- GPU acceleration
- React frontend
- streaming generation
- multi-language support

---

# 🧠 Philosophy

Most people focus on models.

I’m more interested in systems.

This project explores:
- AI orchestration
- multimedia pipelines
- local-first tooling
- generative interfaces

through a simple product experience.

---

<div align="center">

# ⚡ Built With Curiosity

Local-first AI systems are underrated.

</div>

---

# 📜 License

MIT
