import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7

GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)
while True:

    if GPIO.input(pirPin) == GPIO.LOW:

        print ("Motion detected!")

    else:

        print ("No motion")

    time.sleep(0.2)