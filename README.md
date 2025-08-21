Jarvis Voice Assistant 🎙️🤖

This is a Python-based voice assistant inspired by Jarvis.
It listens to your voice commands, performs quick actions (like opening websites), and uses the DeepSeek model (via Ollama) for intelligent responses.
Jarvis also speaks back using Google Text-to-Speech (gTTS).

Features ✨

🎤 Voice Activation → Say "Jarvis" to activate.
🌐 Web Actions:
"open google" → Opens Google
"open youtube" → Opens YouTube
"open facebook" → Opens Facebook

🧠 AI Responses:
For any other command, Jarvis queries DeepSeek (via Ollama).

🔊 Text-to-Speech:
Uses gTTS to speak responses aloud.

🧹 Cleans AI Output:
Removes unnecessary <think>...</think> or [thinking...] text.

Requirements ⚙️
Python 3.x
Microphone access

Installed dependencies:
pip install speechrecognition gTTS requests

Ollama installed with DeepSeek model pulled:
ollama pull deepseek-r1

Example 🕹️
Listening...
Jarvis Activated...
Jarvis (speaking): Opening YouTube

or

Listening...
Jarvis Activated...
Jarvis (speaking): The capital of France is Paris.

Limitations ⚠️
Requires internet for speech recognition and gTTS.
Ollama with DeepSeek must be installed locally.
Only supports English (by default).

Author ✨
Created by Anshul Prasashya.
Feel free to fork, improve, and contribute! 🚀
