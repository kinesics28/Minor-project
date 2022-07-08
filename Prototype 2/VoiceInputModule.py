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


def speechToText(duration=3):

    # initialize the recognizer
    r = sr.Recognizer()
    x=''
    print("Please talk")
    with sr.Microphone() as source:
        #listen for 1 second to calibrate the energy threshold for ambient noise levels
        audio_data = r.adjust_for_ambient_noise(source) 

        # read the audio data from the default microphone
        #audio_data = r.listen(source)

        audio_data = r.record(source, duration=duration)
        print("Recognizing...")
        # convert speech to text
        x = r.recognize_google(audio_data)
        return(x)

def chatMessage():
    r = sr.Recognizer()
    x=''
    print("Please say your message")
    with sr.Microphone() as source:

        #listen for 1 second to calibrate the energy threshold for ambient noise levels
        audio_data = r.adjust_for_ambient_noise(source)

        # read the audio data from the default microphone
        audio_data = r.record(source)
        print("Recognizing...")
        # convert speech to text
        x = r.recognize_google(audio_data)
        return(x)


if __name__ == '__main__':

    print(speechToText())