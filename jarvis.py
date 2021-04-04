import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print (voices[0].id)
engine.setProperty('voice',voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour) 
    if hour>=0 and hour <12:
        speak("good morning")

    elif hour >=12 and hour <18:
        speak("good afternoon")

    else:
        speak("good evening")
    speak("i am jarvis. please tell me how may i help you") 
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) 


    try:
        print("Recognising....")
        query = r.recognize_google(audio, language = 'en-in')
        print("User said : {}\n".format(query))
    
    except Exception as e:
        print(e)
        print("say that again please")
        return "None"
    return query
def sendemail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('personalemail@gmail.com','pesonalemailpassword')
    server.sendmail('personalemail.com' , to ,content)
    server.close()

if __name__=="__main__": 
    wishMe()
    while True:
        query =takeCommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
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
            music_dir = 'E:\\music'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak (f"The time is{strTime}")  
        elif 'play video' in query:
            video_dir='E:\\video'
            videos= os.listdir(video_dir)
            print(videos)
            os.startfile(os.path.join(video_dir,videos[0]))
        elif 'open visual studio code' in query:
            codepath="C:\\Users\\ARKAMITA JOARDER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codepath)
        elif 'open spotify' in query:
            codepath="C:\\Users\\ARKAMITA JOARDER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
            os.startfile(codepath)
        elif 'send email to moumita' in query:
            try:
                speak("what should i say")
                content=takeCommand()
                to="targetemail.com"
                sendemail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry there is a problem, i cannot send email")
        elif 'exit' in query:
            speak("this is jarvis signing off. have a good day")
            break

