# Youtube link used for this program: https://youtu.be/AWvsXxDtEkU (creating a virtual assistant by Programming Hero)

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

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
            talk("listening")
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
    command = take_command ()
    if 'play' in command:
        song = command.replace ('play', '')
        talk ('Playing' + song)
        pywhatkit.playonyt (song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk ("The current time is " + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime ('%m %D, %Y')
        talk ("The date today is " + date)
    elif 'date and time' in command:
        date_time = datetime.datetime.now().strftime ('%m %D, %Y %I:%M %p')
        talk (date_time)
    elif 'search for' in command:
        search = command.replace ('search for', '')
        wiki_info = wikipedia.summary(search, 2)
        print (wiki_info)
        talk (wiki_info)
    elif 'how are you' in command:
        talk ("I'm doing great today. How about you?")
    elif 'Im doing fine' in command:
        talk ("That's great to hear.")
    elif 'free today' in command:
        talk ("Not really. I still have a lot to do today.")
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk (joke)
    else:
        talk ("I didn't understand that, please say it again.")

while True:
    run_alexa ()