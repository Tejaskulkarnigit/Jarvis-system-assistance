
import sys
import ntpath
import smtplib
import subprocess
import time
from urllib import request
import cv2
import pyttsx3
import pywhatkit
import query as query
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import os.path
import requests
from requests import get
import datetime
import secure_smtplib
import pyjokes
import pyautogui
import urllib.request
import instaloader
import PyPDF2
import operator
from bs4 import BeautifulSoup
import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube




# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[0].id)  # 0 for male and 0 for male voice



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didn't understand")
        return "None"
    query = query.lower()    
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour<=17:
        speak("good afternoon")
    elif hour>=18 and hour<=24:
        speak("good evening")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('tejaskulkarni216@gmail.com','shreetej@2210')
    server.sendmail('tejaskulkarni216@gmail.com',to,content)
    server.close()

def news():
    urllib.request.urlopen("http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=05e7cb4d79fc4209bb77b14bd373fd52")
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=05e7cb4d79fc4209bb77b14bd373fd52'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth"]
    for ar in articles:
        head.append(ar['title'])
    for i in range (len(day)):
        speak(f"today's{day[i]} news is:{head[i]}") 

def pdf_reader():
    book = open('py3.pdf','rb')
    pdfReader = PyPDF2.PdfReader(book) 
    pages =pdfReader.numPages
    speak(f"Total numbers of pages  in this book {pages}")
    speak("sir pleasae enter the page number, i have to read...")
    pg = int(input("please enter the page no.:"))
    page = pdfReader.getPage(pg)
    text =page.extractText()
    speak(text)   

    
def abs(a):
    "same as abs(a)."
    return abs(a) 
def add(a,b):
    "same as tyhe a+b."
    return a+b
def and_(a,b):
    "same as a&b."
    return a&b
def floordiv(a,b):
    "same as a//b."
    return a//b
def index(a):
    "same as a.__index__()."
    return a.__index__()
def inv(a):
    "same as a."
    return a
invert = inv
def lshift(a,b):
    "same as a<<b."
    return a<<b
def mod(a,b):
    "same as a%b."
    return a%b
def mul(a,b):
    "same as a*b."
    return a*b                

def TaskExecution():
    wish()
    
    speak("jarvis your personal assistance activeted")
    speak(" i am always there for you ,sir") 
    speak("How can i help you")
    
    while True:
        query = take_command().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")

            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        
        elif 'who are you' in query:
            speak("I am jarvis developed by Tejas")
        elif 'hello 'in query or 'bruhh'in query or 'hi' in query:
            speak("hello Tejas  sir,may i help you something") 
        elif'thank you'in query:
            speak("mention not sir, it's my pleasure")      

        elif'how are you' in query :
            speak ("i am good and what about you sir")
        elif'also good'in query or 'i am okay'in query or 'i am fine' in query:
            speak("that's great ,sir")
            
        
             
                        
        
        elif 'play song on youtube' in query:
            speak("which song ,sir")
            cm = take_command().lower()
            webbrowser.open(f"{cm},youtube.com")
            pywhatkit.playonyt(f"{cm}")
        
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("opening google")
            speak("sir,what should i search on google")
            cm = take_command().lower()
            webbrowser.open(f"{cm},google.com")
        
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        
        elif 'open notepad' in query:
            speak("opening notepad")
            ntpath ="C:\\Windows\\system32\\notepad.exe"
            os.startfile(ntpath)
        
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        
        elif 'open camera' in query:
            speak("opening camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k= cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        
        elif 'email to tejas' in query:
            try:
                speak("what should i say ?,sir")
                content = take_command().lower()
                to ="tejaskulkarni216@gmail.com"
                sendEmail(to.content)
                speak("Email has been sent to tejas")
            except Exception as e:
                print(e)
                speak("sorry sir,i am not able to sent this email to tej")

        elif 'tempreature update'in query:
            search="tempreature in pune"
            url =f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current{search} is {temp}")


        elif 'you can sleep' in query:
            speak("thanks for using me sir, have a good day")
            
        
        elif'close notepad'in query:
            speak("okay sir")
            os.system("taskkill/f/im notepad.exe")
        
        elif'set alarm'in query:
            nn= int(datetime.datetime.now().hour)
            if nn==22:
                music_dir='c:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
        
        elif' tell me a joke' in query:
            speak("sure sir")
            joke = pyjokes.get_joke()
            speak("joke")

        elif'switch the window'in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt") 

        elif'tell me news'in query:
            speak("please wait sir, featching the latest news")
            news()       
        elif 'sleep now' in query or 'you can sleep jarvis' in query:
            speak("okay sir, i am going to sleep you can call me anytime")
            break

# to find my location using IP address
        elif'where i am'in query or 'where we are' in query:
            speak("wait sir, let me cheak")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"sir,i am not sure ,but our current location in{city} city of {state} state of {country} country")
            except Exception as e:
                speak("sorry sir, due to network issues ,i am not able to find where we are ") 
                pass 

# to check a instagram profile 
        elif"instagram profile" in query or "profile on instagram" in query:
            speak("sir, please enter the username correctly.")
            name = input("Enter the username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir,here is the profile of the user {name}")
            time.sleep(5)
            speak("sir, wouyld you like to download profile pic of this account.")
            condition = take_command().lower()
            if "yes" in condition or query:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile pic is saved in main folder , now i am ready for next task")
            else:
                pass    
   
# to take ss
        elif "take a screenshot "in query or "jarvis take a shot"in query:
            speak("sir, please tell me the name for the screenshot file")
            name=take_command().lower()
            speak("please hgold the screen for few seconds,sir,i am taking shot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, screenshot is saved in main folder , now i am ready for next task")

# PDF reader             
        elif"read pdf" in query:
            pdf_reader()
            
# calculate using voice command
        elif"do some calculation" in query or "can you calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what you want to calculate, example")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' :operator.add,
                    '-':operator.sub,
                    '*' :operator.mul,
                    'divided':operator.__truediv__,
                 }[op]
            def eval_binary_expr(op1,oper,op2):
                op1,op2=int(op1),int(op2)
                return get_operator_fn(oper)(op1,op2)
            speak("your result is ")
            speak(eval_binary_expr(*(my_string.split())))

        elif'video downloader'in query or 'jarvis open video downloader'in query:
            root =Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube vedio Downloader")
            speak("enter the link ,sir")
            Label(root,text="Youtube vedio Downloader",font='arial 15 bold').pack()
            link = StringVar()
            Label(root,text="please yt url here",font='arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable=link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.stream.first()
                video.download()
                Label(root,text ="downloaded",font='arial 15').place(x=180,y=210)

            Button(root,text ="Download",font='arial 15 bold', bg ='pale violet red',padx=2,command=VideoDownloader).place(x=180,y=150)
            root.mainloop()
            speak("video downloaded ")       

            
       

        
           
if __name__ == '__main__':
    while True:
        permission = take_command()
        if"wake up jarvis" in permission or "wake up" in permission:
            TaskExecution()
        elif"goodbye jarvis" in permission:
            speak("thank u for using me ,sir, have a good day")
            exit(0)

        
            