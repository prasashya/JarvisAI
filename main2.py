import speech_recognition as sr
import webbrowser
from gtts import gTTS
import os
import requests
import json
import tempfile
import subprocess
import re



def speak(text):
    if text and text.strip():
        print("Jarvis (speaking):", text)
        temp_file = os.path.join(tempfile.gettempdir(), "jarvis_speech.mp3")
        tts = gTTS(text=text, lang='en')
        tts.save(temp_file)
        os.system(f'start {temp_file}')  
    else:
        print("⚠️ Nothing to speak")


def query_deepseek(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "deepseek-r1"],
            input=prompt,  
            text=True,
            capture_output=True,
            encoding="utf-8"
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Ollama failed: {e}"


def clean_reply(text):
    # If DeepSeek outputs "...done thinking." keep only what comes after
    if "...done thinking." in text:
        text = text.split("...done thinking.", 1)[1]
    # Remove <think>...</think> blocks if present
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    # Remove any [thinking...] or (thinking...) parts
    text = re.sub(r"\[thinking.*?\]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\(thinking.*?\)", "", text, flags=re.IGNORECASE)
    return text.strip()


def processCommand(c):
    c_lower = c.lower()
    if "open google" in c_lower:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open youtube" in c_lower:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open facebook" in c_lower:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    else:
        reply = query_deepseek(c)
        reply=clean_reply(reply)
        speak(reply)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
            word = recognizer.recognize_google(audio).lower()

            if "jarvis" in word:
                # speak("Ya?")
                with sr.Microphone() as source:
                    print("Jarvis Activated...")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("Speech API unavailable:", e)
        except Exception as e:
            print("Error:", e)
