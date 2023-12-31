import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
while True:
    with speech_recognition.Microphone() as mic:    
        print("Robot:I'm listening")
        audio = robot_ear.listen(mic)

    print("Robot: ...")

    try:    
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    
    print("You:" + you)

    if you == "hello":
        robot_brain = "Hello"
    elif you == "hi":
        robot_brain = "Hello"
    elif you == "":
        robot_brain = "I can't hear you, try again"
    elif you == "what day is today":
        today = date.today()    
        robot_brain = today.strftime("%B %d, %Y")
    elif you == "what time is it":
        now = datetime.now()
        robot_brain = ("Is %H hours %M minutes %S second")   
    elif you == "how are you":
        robot_brain = "Im fine, thank you"
    elif you == "help":
        robot_brain = "you should read the manual in the file for more infomation!"
    elif you == "update":
        robot_brain = "This is the latest version!"   
    elif you == "goodbye":
        robot_brain = "goodbye!"
        break
    else:
        robot_brain = "I don't know, try another question or call help"
    
print("Robot:" + robot_brain)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
