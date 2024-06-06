import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


# taking voice from my system

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
print(voices[1].id)
print(type(voices))
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',250)




#speak function

def speak(text):
    
    engine.say(text)
    engine.runAndWait()


#speak("my name is kavitha")

#speech recognition

def takeCommand():
    """this function recognize voice and returns text"""

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)


        try:
            print("recognizing...")
            query=r.recognize_google(audio, language='en-in')
            print(f"user said:{query}\n")

        except Exception as e:
            print("say that again please")
            return "none"
        return query
    

text=takeCommand()

speak(text)


