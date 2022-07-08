from pynput.keyboard import Key, Controller
import time

import speech_recognition as sr


keyboard = Controller()
def mic():
    #time.sleep(2)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('d')

def video():
    #time.sleep(2)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('e')

def speechToText(x):
    duration = 3

    # initialize the recognizer
    r = sr.Recognizer()
    x=''
    print("Please talk")
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=duration)
        print("Recognizing...")
        # convert speech to text
        x = r.recognize_google(audio_data)
        return(x)

x=''

while(True):
    x=''
    try:
        x=speechToText(x)
    except:
        pass

    print(x)

    if x=='turn on mic' or x=='mic on' or x=='turn on my mic' or x=='turn on Mike' or x=='Mike on' or x=='turn on my Mike' or x=='microphone off' or  x=='microphone on':
        mic()
        x=''

    elif x=='turn off mic' or x=='mic off' or x=='turn off my mic' or  x=='turn off Mike' or x=='Mike off' or x=='turn off my Mike':
        mic()
        x=''


    elif x=='turn on camera' or x=='camera on' or x=='turn on my camera' or x=='turn on video' or x=='video on' or x=='turn on my video' or x=='':
        video()
        x=''

    elif x=='turn off camera' or x=='camera off' or x=='turn off my camera' or x=='turn off video' or x=='video off' or x=='turn off my video' :
        video()
        x=''

    elif x=='stop listening':
        break
    else:
        pass
    
