import speech_recognition as sr
from gtts import gTTS
import os

def say(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("mpg123 output.mp3")

def stt():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         r.pause_threshold = 1
         audio = r.listen(source)
         query = r.recognize_google(audio, language='en')
         print(f'User said : {query}')
         return query

if __name__ == '__main__':
    say("Hello Samarth, what can I do for you?")
    text = stt()
    say(text)
