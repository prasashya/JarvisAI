from gtts import gTTS
import os

tts = gTTS("Hello, this is a test")
tts.save("output.mp3")
os.system("start output.mp3")  # Windows
