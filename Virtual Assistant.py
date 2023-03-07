# import pylance
import speech_recognition as sr
import wikipedia as wk
import pyaudio
import pyttsx3
import datetime
import webbrowser as wb
import os
from random import random
import smtplib as smt
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)  Name of the voice of the female AI
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning BOSS!")
    elif hour>=12 and hour<=16:
        speak("Good Afternoon BOSS!")
    elif hour>=16 and hour<=20:
        speak("Good Evening BOSS!")
    else:
        speak("Good Night BOSS")
    speak("How can I help you?")
def takeCommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold=1
            r.energy_threshold=400
            audio=r.listen(source)
        try:
            print("Recognizing....")
            query=r.recognize_google(audio, language='en-in')
            print("User said: ", query)
        except Exception as e:
            # print(e)
            print("Please repeat sir...")
            return "None"
        return query
def sendEmail(to, content):
    server=smt.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__==  "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wk' in query:
            speak("Searching wikipedia")
            query=query.replace("wikipedia", "")
            results=wk.summary(query,sentences=2)
            speak("According to Wikipedia")
            # speak(results)
        elif 'open youtube' in query:
            wb.open("youtube.com")
        elif 'open google' in query:
            wb.open("google.com")
        elif 'play music' in query:
            wb.open("spotify.com")
        elif 'nothing' in query:
            speak("ok sir")
            exit()
        
        elif 'play music on player' in query:
            song_dir="D:\songs NC"
            songs=os.listdir(song_dir)
            # print(songs)
            #os.startfile(os.path.join(song_dir,random.randint.songs))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        elif 'open vs code' in query:
            codePath="C:\\Users\\gauta\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'send mail to' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="gautamjangir2002@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("The email has not been sent")
        elif 'shut down' in query:
            exit()