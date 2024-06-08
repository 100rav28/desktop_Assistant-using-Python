import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS



GOOGLE_API_KEY="****************************"

os.environ['GOOGLE_API_KEY']=GOOGLE_API_KEY

def voice_input():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise and record audio
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)
            return text
        except sr.RequestError:
            print("API request failed")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        


def text_to_speech(text, lang='en'):
    # Initialize gTTS object
    tts = gTTS(text=text, lang=lang, slow=False)

    # Save the speech to a file
    filename = "output.mp3"
    tts.save(filename)

    # Play the speech
    os.system(f"start {filename}")  # Use "mpg321" on Linux or "afplay" on macOS

def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model=genai.GenerativeModel('gemini-pro')
    
    response=model.generate_content(user_text)
    
    result=response.text
    
    return result
