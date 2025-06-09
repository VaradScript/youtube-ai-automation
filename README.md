# 🎬 YouTube AI Automation Workflow (n8n + Flask + AI)

This project automates the full content creation pipeline for **YouTube videos** using AI.  
It integrates OpenRouter for AI text generation, gTTS for voiceovers, and custom Python Flask services for **script-to-audio** and **script-to-subtitles (SRT)**.  
All processes are orchestrated using **n8n**, hosted locally via Docker.

> ✅ Ideal for faceless YouTube automation, content repurposing, or rapid short-form video generation.

---

## 🧠 What It Does

- ✍️ Generates **AI-written video scripts**
- 🎙 Converts scripts into **audio (MP3)** using TTS
- 📄 Converts scripts into **subtitles (SRT format)**
- 🖼 Generates **AI images/videos** from prompts (via API)
- 🎥 Combines assets for complete YouTube-ready content
- 🧩 Runs using a visual workflow in **n8n**

---

## 🖼 Workflow Diagram

![Workflow Preview](screenshots/yt.png)

- **Top Area** = API setup (AI images, videos)
- **Bottom Area** = Local services (script, audio, subtitle)
- **Left Area** = Entry point (video idea → AI flow)

---


---

## 🐳 How to Run n8n with Docker

Run n8n locally on port `5678` and mount persistent storage:

```bash
docker run -it --rm -p 5678:5678 -v C:\Users\gamin\.n8n:/home/node/.n8n n8nio/n8n       ** add your path
```

🧪 Running Flask Services
📜 1. Script-to-SRT (Subtitles)
```bash
cd services/
python script-to-srt.py
```

🔊 2. Text-to-Speech (Audio)
```
cd services/
python text-to-speech.py

```

💡 Use Cases
🧠 Faceless YouTube channel automation

📰 Blog-to-YouTube conversion

📈 Short-form content generation with voice & captions

🎥 Bulk video generation pipelines

