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
    

#text=takeCommand()

#speak(text)
def wish_me():
    hour=(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir.how are you doing")

    elif hour>=12 and hour<18:
        speak("good afternoon sir.how are you doing")

    else:
        speak("good evening sir how are you doing")

    speak("i am JARVIS.Tell me sir how can i help you")

if __name__=="__main__":

    wish_me()
    while True:
        query=takeCommand().lower()
        # print(query)

        if "wikipedia" in query:
            speak("searching wikipedia")
            query=query.replace('wikipedia',"")
            print(query)
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
            
            
            
            
        elif 'time' in query:
            strtTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strtTime}")
            
        elif 'goodbye' in query:
            speak("ok sir.bye bye")
            exit()
            
            
            
       

    
  

    