import speech_recognition as sr
import webbrowser
import requests
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Sir please speak something ....")
        audio=r.listen(source)
        text=r.recognize_google(audio)
        print("Sir you said {}".format(text))
        return text
number=takeCommand()
url="https://www.google.com/search?q=" + number
webbrowser.get().open(ur1)