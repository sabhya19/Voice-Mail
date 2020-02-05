import speech_recognition as s_r
import pyttsx3
import pyaudio
import winsound
import msvcrt as m
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
frq=400
dur= 700
engine = pyttsx3.init() 
engine.setProperty('rate',150)
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
engine.say("welcome to; Sig no mail; mailing system")
engine.say(";;Press enter to start running the tool")
engine.runAndWait()
def wait():
    m.getch()
input("please press enter to continue")
engine = pyttsx3.init() 
engine.say(" you have prompted sig no mail; please follow and respond to furthur requests;")
engine.runAndWait()
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
with my_mic as source:
    print("Please choose an option...")
    engine = pyttsx3.init() 
    engine.say("speak A to open gmail;; speak B to escape to google;")
    engine.runAndWait()
   # winsound.Beep(frq,dur)
    my_option = r.listen(source,timeout=5) #take voice input for mailing ID
my_option= r.recognize_google(my_option)
print(my_option)
if my_option=='a' or 'A' :
    with my_mic as source:
     print("Please speak your email ID")
     engine = pyttsx3.init() 
     engine.say("please speak your email I D ;")
     engine.runAndWait()
     winsound.Beep(frq,dur)
     my_id = r.listen(source)# take input content to send on to teh other side
     content= r.recognize_google(my_id)# converting said content to text  
    print(my_id)
    browser = webdriver.Chrome()
    browser.get(('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Ftab%3Drm%26ogbl&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession'))
elif my_option=='b' or 'B' :
    browser = webdriver.Chrome()
    browser.get(('http://www.google.com'))
else :
    engine = pyttsx3.init() 
    engine.say("Sorry! Could not process your request.")
    engine.runAndWait()


  