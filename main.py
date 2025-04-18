import speech_recognition as sr
import pyttsx3

# from gtts import gTTS
# import os
# import webbrowser as wb
#
# def say(text):
#     tts = gTTS(text=text, lang='en')
#     tts.save("output.mp3")
#     os.system("mpg123 output.mp3")
#
# def stt():
#      r = sr.Recognizer()
#      with sr.Microphone() as source:
#          r.pause_threshold = 1
#          audio = r.listen(source)
#          try:
#             query = r.recognize_google(audio, language='en')
#             print(f'User said : {query}')
#             return query
#          except Exception as e:
#              return "Some error occurered"
#
# if __name__ == '__main__':
#     say("Hello Samarth, what can I do for you?")
#     while(True):
#      text = stt()
#      say(text)








from services.askgroq import ask_groq
from utils.commandParser import parse_command


engine = pyttsx3.init()



def stt():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         r.pause_threshold = 1
         audio = r.listen(source)
         try:
            query = r.recognize_google(audio, language='en')
            print(f'User said : {query}')
            return query
         except Exception as e:
             return "Some error occurered"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    print("🎯 AI Assistant is running. Say something!")

    while True:
        user_input = stt()
        print(user_input)

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye!")
            break

        command = parse_command(user_input)

        if command['type'] == "music":
            print(f"🎵 (Pretend) Playing music: {command['query']}")
            # Later: connect real Spotify player
        elif command['type'] == "image":
            print(f"🎨 (Pretend) Generating image: {command['prompt']}")
            # Later: call DALL-E or SD API
        elif command['type'] == "email":
            print("✉️ Writing Email...")
            response = ask_groq(f"Write an email with the following instruction: {command['prompt']}")
            print("\nGenerated Email:\n", response)
        else:
            response = ask_groq(command['prompt'])
            print("\nAssistant:", response)
            speak(response)

if __name__ == "__main__":
    main()

