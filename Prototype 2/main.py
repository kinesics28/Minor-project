from controlFunctions import meetLogin, mic, video ,openChat,paste, clear, send , closeChat
from VoiceInputModule import speechToText, chatMessage


# take input from GUI
mail_address="testforminorproject@gmail.com"
password="minorproject"


def confirmspeech(x=3):
    try:
        return speechToText(x)
    except:
        return confirmspeech()

def sendmessage():
    clear()
    paste("Please say your message")
    
    #message=chatMessage()   # use when absoulute silence
    try:
        message=speechToText(5)
    except:
        sendmessage()
    clear()
    paste(message + "----Do you want to send?")

    confirmation=confirmspeech()
    
    clear()
    if confirmation == 'Yes' or 'yes':
        paste(message)
        send()
    elif confirmation =='No' or 'no':
        sendmessage()


def hearCommand():
    while(True):
        x='try again'
        try:
            x=speechToText()
        except:
            pass

        print(x)
        micon=['turn on mic','mic on' ,'turn on my mic' ,'turn on Mike' ,'Mike on','turn on my Mike','microphone off','microphone on','microphone of','turn on my','Mike']
        micoff=['turn off mic' ,'mic off' ,'turn off my mic' ,'turn off Mike' ,'Mike off' ,'turn off my Mike','Mike' ]
        camon=['turn on camera' ,'camera on' ,'turn on my camera','turn on video','video on' ,'turn on my video']
        camoff=['turn off camera' ,'camera off' ,'turn off my camera' ,'turn off video' ,'video off' ,'turn off my video' ,'video of']
        chat=['write in chat','chatbox','write in chatbox','chat box','write in chat box','open chatbox','open chat box','open chat','Titan chart','chat']

    
        # if x=='turn on mic' or x=='mic on' or x=='turn on my mic' or x=='turn on Mike' or x=='Mike on' or x=='turn on my Mike' or x=='microphone off' or  x=='microphone on' or x=='microphone of':
        #     mic()
        #     x=''

        # elif x=='turn off mic' or x=='mic off' or x=='turn off my mic' or  x=='turn off Mike' or x=='Mike off' or x=='turn off my Mike' :
        #     mic()
        #     x=''


        # elif x=='turn on camera' or x=='camera on' or x=='turn on my camera' or x=='turn on video' or x=='video on' or x=='turn on my video' or x=='':
        #     video()
        #     x=''

        # elif x=='turn off camera' or x=='camera off' or x=='turn off my camera' or x=='turn off video' or x=='video off' or x=='turn off my video' or x=='video of':
        #     video()
        #     x=''

        # elif x=='stop listening':
        #     break
        # else:
        #     pass

        if x in micon:
            mic()
            x=''

        elif x in micoff:
            mic()
            x=''

        elif x in camon:
            video()
            x=''

        elif x in camoff:
            video()
            x=''

        elif x in chat:
            openChat()
            sendmessage()
            closeChat()
        
        elif x=='stop listening':
            break
        else:
            pass
    


if __name__=='__main__':

    mail_address="testforminorproject@gmail.com"
    password="minorproject"

    meetLogin(mail_address,password)
    hearCommand()

    

