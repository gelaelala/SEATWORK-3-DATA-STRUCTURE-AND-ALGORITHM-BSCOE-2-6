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
            listen = "Listening..."
            print (listen)
            talk (listen)
            print ()
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace ('alexa', '')
                print (command)
                print ()
    except:
        pass
    return command

def run_alexa ():
    command = take_command ()
    if 'play' in command:
        song = command.replace ('play', '')
        song_play = 'Playing' + song
        print (song_play)
        print()
        talk (song_play)
        pywhatkit.playonyt (song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        time_today = "The current time is " + time
        print (time_today)
        print()
        talk (time_today)
    elif 'date' in command:
        date = datetime.datetime.now().strftime ('%B %d, %Y')
        date_today = "The date today is " + date
        print (date_today)
        print()
        talk (date_today)
    elif 'search for' in command:
        search = command.replace ('search for', '')
        wiki_info = wikipedia.summary(search, 2)
        print (wiki_info)
        print()
        talk (wiki_info)
    elif 'how are you' in command:
        great = "I'm doing great today."
        print (great)
        print()
        talk (great)
    elif 'free today' in command:
        free = "Not really. I still have a lot to do today."
        print (free)
        print()
        talk (free)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print (joke)
        print()
        talk (joke)
    else: 
        say = "I didn't understand that, please say it again."
        print (say)
        print ()
        talk (say)

while True:
    run_alexa ()