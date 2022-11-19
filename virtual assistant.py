# Youtube link used for this program: https://youtu.be/AWvsXxDtEkU (creating a virtual assistant by Programming Hero)

import speech_recognition as sr

listener = sr.Recognizer ()
try:
    with sr.Microphone () as source:
        print ('Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
except:
    pass