#Libraries required
import speech_recognition
import smtplib,ssl
import pyttsx3

Ymail = ""
Ypass = ""
Rmail = ""
Mbdy = ""


recog=speech_recognition.Recognizer()
speeker=pyttsx3.init()
speeker.setProperty('rate',150)

portnumber = 465


def ListenToAudio():  #Function for taking audio from microphone as source
    mic=speech_recognition.Microphone()
    with mic as source:
        print('You can speak now: ')
        recgnise = speech_recognition.Recognizer()
        recgnise.adjust_for_ambient_noise(source)
        speech = recgnise.listen(source)
    return speech


def TranslateTheAudio():  #Function to translate the audio into text using google speech recognition api
    try:
        xtr = ListenToAudio()
        xtr1 = recog.recognize_google(xtr)
        xtr2 = str(xtr1).lower()
        trnsltd = xtr2
        return trnsltd
    except:
        print("Please try again... ")
        return TranslateTheAudio()


def SpeakThePhrase(s):  #Function to wait for the user to speak
    print(s)
    speeker.say("I got that, "+s)
    speeker.runAndWait()
    

def YourEmlId():  #Function to take input for User's Email
    Ymail = ""
    print("Please input your Email: ")
    Extra = TranslateTheAudio()
    for i in Extra.split(" "):
        Ymail = Ymail+i
    SpeakThePhrase(Ymail)
    print("Want to correct anything?")
    spokn = TranslateTheAudio()
    SpeakThePhrase(spokn)
    if "yes" in spokn:
        return YourEmlId()
    else:
        return Ymail


def YourEmlPassword():  #Function to take input for User's Password
    Ypass = ""
    print("Please input Your Password: ")
    Extra = TranslateTheAudio()
    for i in Extra.split(" "):
        Ypass = Ypass+i
    SpeakThePhrase(Ypass)
    print("Want to correct anything?")
    spokn = TranslateTheAudio()
    SpeakThePhrase(spokn)
    if 'yes' in spokn:
        return YourEmlPassword()
    else:
        return Ypass

#Function to take input for Reciever's Email
def RecEmlId():
    Rmail = ""
    print("Please input the Receiver's Email: ")
    Extra =  TranslateTheAudio()
    for i in Extra.split(" "):
        Rmail = Rmail+i
    SpeakThePhrase(Rmail)
    print("Want to correct anything?")
    spokn = TranslateTheAudio()
    SpeakThePhrase(spokn)
    if 'yes' in spokn:
        return RecEmlId()
    else:
        return Rmail

#Function to take input for the body of the Email
def MailBody():
    print("Please input the Email Body: ")
    Mbdy = TranslateTheAudio()
    print("Want to correct anything?")
    spokn = TranslateTheAudio()
    if 'yes' in spokn:
        return MailBody()
    else:
        return Mbdy

#main function
print('Ask to "Open My Gmail on PC"')
speeker.say('Ask to "Open My Gmail on PC"')
speeker.runAndWait()
spokn1 = TranslateTheAudio()
SpeakThePhrase(spokn1)
spokn = ''
if 'gmail' in spokn1:
    print("I got that, ",spokn1)
    Ymail = YourEmlId()
    Ypass = YourEmlPassword()
    Security = ssl.create_default_context()
    print("Gmail will be opened soon...")
    SpeakThePhrase("Gmail will be opened soon...")
    speeker.runAndWait()
    print('Lets start with a new mail... \nDo you want to write one?')
    SpeakThePhrase('Lets start with a new mail... \nDo you want to write one?')
    speeker.runAndWait()
    spokn2 = TranslateTheAudio()
    SpeakThePhrase(spokn2)
    if 'yes' in spokn2:
        Rmail = RecEmlId()
        Mbdy = MailBody()
        with smtplib.SMTP_SSL("smtp.gmail.com",portnumber ,context=Security) as server:
            server.login(Ymail,Ypass)
            server.sendmail(Ymail,Rmail,Mbdy)
