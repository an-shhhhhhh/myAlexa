import datetime

import pyjokes
import speech_recognition as sr #recognise speech
import pyttsx3 #makes alexa talk to humans
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer() #understands the audio said by the user
engine = pyttsx3.init()
voices = engine.getProperty('voices') #by default alexa has a male voice ,so to convert it into another voice we use this line
engine.setProperty('voice', voices[1].id) #we have a male voice at index 0, and female voice at index 1
engine.say('Hi! I am alexa')
engine.say('and i promise to only work for you')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....') #command to be printed on the screen indicating that alexa is listening to my voice
            voice = listener.listen(source) #using microphone as source and calling speech recognizer to listen to this source
            command = listener.recognize_google(voice) #using google voice recoginzer api to convert the audio just listened into text
            command = command.lower()
            if 'alexa' in command:#will print the audio only if alexa is mentioned in the audio
                command = command.replace('alexa','')#it may happen that alexa word is not mentioned in user's audio
                talk(command) #prints the audio converted into text|
    except:
        pass #python will ignore or do not do anything when exception# happens
    return command

def run_alexa():
    command = take_command() #variable command is calling function take_command
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song) # song will play on youtube

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') #print the current time from datetime package
        print(time)
        talk('Current time is '+time)

    elif 'who the heck is ' in command:
        person = command.replace('who the heck is','')
        info = wikipedia.summary(person,1) #information about the person will be searched and it will print only 1 line of information
        print(info) #prints the info
        talk(info) #also talks about the info

    elif 'are you single' in command:
        talk('Sorry dear! I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Sorry I could not hear it ...beg pardon')

while True: # alexa will not die , as it is stuck in an endless loop
    run_alexa()