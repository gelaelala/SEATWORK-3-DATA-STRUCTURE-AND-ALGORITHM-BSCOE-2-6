# Youtube link used for this program: https://youtu.be/AWvsXxDtEkU (creating a virtual assistant by Programming Hero)

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer ()
engine = pyttsx3.init ()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say (text)
    engine.runAndWait ()

def take_command ():
    try:
        with sr.Microphone () as source:
            print ('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace ('alexa', '')
                print (command)
    except:
        pass
    return command

def run_alexa ():
    command = take_cammand ()
    print (command)
    if 'play' in command:
        song = command.replace ('play', '')
        talk ('Playing' + song)
        pywhatkit.playonyt (song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk ("The current time is " + time)
    elif 'search for' in command:
        search = command.replace ('search for', '')
        wiki_info = wikipedia.summary(search, 2)
        print (wiki_info)
        talk (wiki_info)

run_alexa ()