import requests 
import RPi.GPIO as GPIO
import time

def motion_detected():
    t = time.localtime()
    print("%d:%d:%d Motion Detected" % (t.tm_hour, t.tm_min, t.tm_sec))
    requests.post('https://maker.ifttt.com/trigger/motion_detected/json/with/key/d5GSlrdgYExPUXVpg8M5acWIdmlqlLLE-mDnodY9gPG')
    requests.get('http://127.0.0.1:5000/push_capture')

def motion_not_detected():
    t = time.localtime()
    print("%d:%d:%d No motion" % (t.tm_hour, t.tm_min, t.tm_sec))

GPIO.setmode(GPIO.BCM)
pin = 7
GPIO.setup(pin, GPIO.IN)
try:
    print ("Waiting for sensor to settle...")
    print ("PIR modul test (CTRL+C to exit")
    time.sleep(1)
    print ("Detecting motion...")
    
    while True:
        
        if GPIO.input(pin):
            motion_detected()
            
        else:
            motion_not_detected()
        time.sleep(3)

except KeyboardInterrupt:
    GPIO.cleanup()
print ("Quit")
