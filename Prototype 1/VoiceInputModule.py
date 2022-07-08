import speech_recognition as sr
#import sys

""" 
#read duration from the arguments
#duration = int(sys.argv[1])
duration = 3

# initialize the recognizer
r = sr.Recognizer()
print("Please talk")
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=duration)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text) 

"""

def speechToText(x):
    duration = 2

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
print(speechToText(x))