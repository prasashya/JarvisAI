import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
import json

tts=pyttsx3.init()
def speak(text):
    tts.say(text)
    tts.runAndWait()
newsapi="f90cf125b1c34f55bff68962ada45139"
def ask_ollama(prompt):
    try:
        res = requests.post("http://localhost:11434/api/generate",
                            json={"model": "llama3", "prompt": prompt},
                            stream=True)
        output = ""
        for line in r.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    output += data["response"]
        return output.strip()
    except Exception as e:
        print("Ollama failed:", e)
        return "I couldnt process that right now."
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open porn" in c.lower():
        webbrowser.open("https://www.xnxx.com/")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data["articles"]

            print("\nTop Headlines:\n")
            for i, article in enumerate(articles[:5], 1):
                headline = article["title"]
                print(f"{i}. {headline}")   # <-- prints in console
                speak(headline)             # <-- speaks out loud
        else:
            print("Failed to fetch news:", r.status_code)
            speak("Sorry, I could not fetch the news.")


    else:
        reply=ask_ollama(c)
        speak(reply)

if __name__=="__main__":
    speak("Initializing Jarvis....")
    r = sr.Recognizer()
    while(True):
        # Listen for the wake word jarvis
        # obtain audio from the microphone
        
        
        
        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening...!")
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                
            word=r.recognize_google(audio)
            word=word.lower()
            if "jarvis" in word:
                speak("Yes Sir ")
                
                #listen for commannd
                with sr.Microphone() as source:
                    print("Jarvis Activate...!")
                    
                    r.adjust_for_ambient_noise(source,duration=0.2)
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    print(command)
                    processCommand(command)
        
        except Exception as e:
            print("error; {0}".format(e))