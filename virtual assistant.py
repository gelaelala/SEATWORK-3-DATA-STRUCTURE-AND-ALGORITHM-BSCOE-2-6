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
        with sr.Microphone () as source: # using microphone as the source for the user's command
            listen = "Listening..."
            print (listen)
            talk (listen)
            print ()
            voice = listener.listen(source) # the program will listen to what was the user's saying
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command: # the program will only continue if they hear the word "alexa" during the user's command
                command = command.replace ('alexa', '')
                print (command)
                print ()
    except:
        pass
    return command

def run_alexa ():
    command = take_command ()
    if 'play' in command: # the virtual assistant will play the song in Youtube with the help of pywhatkit
        song = command.replace ('play', '')
        song_play = 'Playing' + song
        print (song_play)
        print()
        talk (song_play)
        pywhatkit.playonyt (song)
    elif 'time' in command: # the virtual assistant will tell the time (format of time will be in hours:minutes and is stated in 12-hour format instead of 24-hour format (e.g. 12:22 PM))
        time = datetime.datetime.now().strftime('%I:%M %p')
        time_today = "The current time is " + time
        print (time_today)
        print()
        talk (time_today)
    elif 'date' in command: # the virtual assistant will tell the date today (format of date will be in "month" "day", "year" (e.g. November 19, 2022))
        date = datetime.datetime.now().strftime ('%B %d, %Y')
        date_today = "The date today is " + date
        print (date_today)
        print()
        talk (date_today)
    elif 'search for' in command: # the virtual assistant will search for the subject in wikipedia and will give a 2-setence summary
        search = command.replace ('search for', '')
        wiki_info = wikipedia.summary(search, 2)
        print (wiki_info)
        print()
        talk (wiki_info)
    elif 'how are you' in command: # the virtual assistant will reply to the user if they heard the "how are you" phrase
        great = "I'm doing great today."
        print (great)
        print()
        talk (great)
    elif 'free today' in command: # the virtual assistant will reply to the user if they heard the "free today" phrase
        free = "Not really. I still have a lot to do today."
        print (free)
        print()
        talk (free)
    elif 'joke' in command: # the virtual assistant will tell the user a joke with the help of pyjokes module
        joke = pyjokes.get_joke()
        print (joke)
        print()
        talk (joke)
    else: # if the user didnt say anything or didnt hear any of the keywords above
        say = "I didn't understand that, please say it again."
        print (say)
        print ()
        talk (say)

while True: # program will loop after each conversation with the virtual assistant
    run_alexa ()