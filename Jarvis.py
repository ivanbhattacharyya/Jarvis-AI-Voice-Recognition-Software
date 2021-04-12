import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('Hi, This is Jarvis')
engine.say('What can I do for you?')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():

    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'Jarvis' in command:
                command = command.replace('Jarvis' , '')
                print(command)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                talk('Current time is' + time)
            elif 'who is' in command:
                person = command.replace('who is' , '')
                info = wikipedia.summary(person , 1)
                print(info)
                talk(info)
            elif 'what is' in command:
                thing = command.replace('what is' , '')
                info2 = wikipedia.summary(thing , 1)
                print(info2)
                talk(info2)
            elif 'joke' or 'jokes' in command:
                talk(pyjokes.get_joke())
            else:
                talk('Please tell me the command again')

    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play' , '')
        talk('playing' + song)
        pywhatkit.playonyt(songwhile True:
)

while True:
        run_jarvis()