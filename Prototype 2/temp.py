# import pyperclip

# x='The text to be copied to the clipboard.'
# pyperclip.copy(x)
# #spam = pyperclip.paste()


import speech_recognition as sr

r = sr.Recognizer()
x=''
print("Please talk")
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.listen(source)
    print("Recognizing...")
    # convert speech to text
    x = r.recognize_google(audio_data)
    print(x)