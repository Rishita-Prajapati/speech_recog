'''import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
import getpass

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def authenticate(username, password):
    # Replace with your own authentication logic
    return username == "admin" and password == "password"

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    speak(text)
    if 'open google' in text.lower():
        webbrowser.open('https://www.google.com')
    elif 'open youtube' in text.lower():
        webbrowser.open('https://www.youtube.com')
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError:
    print("Sorry, the service is down. Please try again later.")

while True:
    text = input("Enter the text you want to convert to speech: ")
    if 'Quit' in text:
        print("Exit")
        break

    if 'open' in text.lower():
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        if authenticate(username, password):
            if 'notepad' in text:
                subprocess.Popen(['notepad.exe'])
            elif 'chrome' in text:
                subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'])
            elif 'youtube' in text.lower():
                webbrowser.open('https://www.youtube.com')
            elif 'calculator' in text:
                subprocess.Popen(['calc.exe'])
            elif 'google' in text.lower():
                webbrowser.open('https://www.google.com')
            elif 'vscode' in text:
                subprocess.Popen(['C:\\Program Files\\Microsoft VS Code\\Code.exe'])
            elif 'whatsapp' in text:
                webbrowser.open('https://web.whatsapp.com')
            elif 'github' in text:
                webbrowser.open('https://github.com')
        else:
            print("Authentication failed. Please try again.")
    else:
        speak(text)
        print("Press 'Quit' to quit or any other key to continue.")'''
import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def authenticate(username, password):
    return username == "admin" and password == "password"

r = sr.Recognizer()

def get_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            speak("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError:
            speak("Sorry, the service is down. Please try again later.")
            return ""

while True:
    speak("Hi, I'm Arina. How can I help you")
    text = get_audio().lower()
    
    if 'quit' in text.lower():
        speak("Exit")
        break

    if 'open' in text:
        speak("Please say your username.")
        username = get_audio()
        
        speak("Please say your password.")
        password = get_audio()

        if authenticate(username, password):
            if 'notepad' in text:
                subprocess.Popen(['notepad.exe'])
            elif 'chrome' in text:
                subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'])
            elif 'youtube' in text:
                webbrowser.open('https://www.youtube.com')
            elif 'calculator' in text:
                subprocess.Popen(['calc.exe'])
            elif 'google' in text:
                webbrowser.open('https://www.google.com')
            elif 'vscode' in text:
                subprocess.Popen(['C:\\Program Files\\Microsoft VS Code\\Code.exe'])
            elif 'whatsapp' in text:
                webbrowser.open('https://web.whatsapp.com')
            elif 'github' in text:
                webbrowser.open('https://github.com')
            speak("Authentication successful. Opening " + text)
        else:
            speak("Authentication failed. Please try again.")
    else:
        speak(text)
        print("Press 'Quit' to quit or say another command.")

