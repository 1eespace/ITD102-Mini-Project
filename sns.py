import RPi.GPIO as GPIO
import time, datetime

from subprocess import call

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
import os

def sendMail():
    sender = "hihowareyoupre88@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, "skehdlwpghwndbgkrtod")

    receivers = ["n11355191@qut.edu.au", "chanyoung.kim@connect.qut.edu.au"] 

    subject = "Smart-Home : Motion Detection Notification!"
  
    msg = MIMEMultipart()

    msg['From'] = sender
    msg['To'] = ", ".join(receivers)
    msg['subject'] = Header(subject, 'utf8')

    body = """\
        <h3> Motion Detect. </h3>
        <p> This mail is automatically sent when movement is detected by the Raspberry Pi sensor. <br>
        <strong> Please check the CCTV on the smart home web page. </strong></p>
        """
import RPi.GPIO as GPIO
import time, datetime

GPIO.setmode(GPIO.BCM)
pin = 26

GPIO.setup(pin, GPIO.IN)

print ("Waiting for sensor to settle...")
time.sleep(2)
print ("Detecting motion...")


while True:
    if GPIO.input(pin) == GPIO.LOW:
        print ("Motion Detected!")
        sendMail()
        time.sleep(2)
    else:
        print ("No motion")
    time.sleep(1)



