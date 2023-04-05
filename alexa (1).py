import datetime

import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
# import vlc
# import pafy
from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


count = 0
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    talk("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    talk(location)
    print(time)
    talk(time)
    print(info)
    talk(info)
    print(weather+"°C")
    talk(weather+"°C")


def hello(count):
     if count == 0:
                talk('Hi, I am  your  virtual assistance. how can i help you')
     else:
                talk('Anything else')
                
def listen_command():

    try:
        with sr.Microphone()as source:
            listener.adjust_for_ambient_noise(source)
            print('listening....')
            listener.pause_threshold = 0.7
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = commad.lower()
            print(command)

    except Exception as e:
        print(e)
        talk("sorry i can't understand,can you speak again")
        return "None"
        
    return command


def take_command(count):
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            hello(count)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'd2' in command:
                command = command.replace('d2', '')
                print(command)
                
    except Exception as e:
        print(e)
        talk("sorry i can't understand,can you speak again")
        return "None"

    return command


# def play(command):
#     song = command.replace('play', '')
#     talk('playing ' + song)
#     url = pywhatkit.playonyt(song)
#     video = pafy.new(url)
#     best = video.getbest()
#     media = vlc.MediaPlayer(best.url)
#     media.play()

def run_d2(count):
    command = take_command(count)
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)                                      # {to paly this on any broswer}

    elif ' how are you' in command:
        talk('I am fine , are you good ?')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif  'read book' in command:
        talk('yes i can read a book')
        talk('which book did you want to listen')
        bookname = listen_command()
        bn = bookname + '.txt'
        f = open(bn, 'r')
        f_text = f.readlines()
        for i in f_text:
            talk(i)
            print(i)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'weather' in command:
        talk('Can you tell me which city you are?')
        city = listen_command()
        city = city+'weather'
        print(city)
        weather(city)
        print("Have a Nice Day:)")
        talk("Have a Nice Day:)")

    elif 'date' in command:
        today = datetime.datetime.now()

        print(today.strftime("%A"))
        print(today.strftime("%d-%m-%Y"))
        talk(today.strftime("%A,%d-%B-%Y"))

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'your name' in command:
        talk('My name is virtual assistance')

    elif 'exit'  in command:
        talk('Thanks for using my service ')
        print('TURN OFF')
        exit()
    elif 'have you ate ' in command:
          talk('just consuming connectivity')


    else:
        talk('Please say the command again.')
        run_d2(count)


while True:
    run_d2(count)
    count += 1
