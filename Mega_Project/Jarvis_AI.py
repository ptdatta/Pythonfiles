import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir,Please tell me how can I help you")

def takeCommand():
    # It takes microphone input from the user and returns the string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        quary=r.recognize_google(audio,language='en-in')
        print(f"User said: {quary}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return quary

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com","your-password")
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishme()
    while(True):
        query=takeCommand().lower()
#       logic for executing tasks based on quary
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='C:\\Users\\parth\\Music\\Planet Pit'
            song=os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[3]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)

        elif 'open code' in query:
            codepath="E:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to harry' in query:
            try:
                speak("what should I say")
                content=takeCommand()
                to="harryyourEmail@gmail.com"
                sendemail(to,content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry sir!I am not able to do it")

        elif 'quit' in query:
            break






