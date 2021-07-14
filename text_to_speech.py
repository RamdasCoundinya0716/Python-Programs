import pyttsx3 #text to speech converter module
import datetime

engine = pyttsx3.init()
voice = engine.getProperty('voice')
voice_rate = 150
engine.setProperty('rate', voice_rate)


def speech(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime('%H hours:%M minutes')
    speech("The current time is :")
    speech(Time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speech("Today's date is : ")
    speech(day)
    speech(month)
    speech(year)


def greet():
    hour = datetime.datetime.now().hour
    if hour in range(6, 13):
        speech("Good Morning Naruto")
    elif hour in range(12, 19):
        speech("Good Afternoon Naruto")
    elif hour in range(18, 22):
        speech("Good evening Naruto")
    else:
        speech("Good Night, Naruto")
    speech("JARVIS at your service. How may i help you?")
    time()
    date()


greet()
