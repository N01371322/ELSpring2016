#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setwarnings(False)

def Blink():
 while True:
 	GPIO.output(23,True)
 	time.sleep(0.1)
 	GPIO.output(23,False)
 	time.sleep(0.1)
	GPIO.output(23,True)
	time.sleep(0.1)
	GPIO.output(23,False)
	time.sleep(0.1)
	GPIO.output(23,True)
	time.sleep(0.1)
	GPIO.output(23,False)
	time.sleep(5)
	GPIO.output(23,True)
        time.sleep(0.1)
	GPIO.output(23,False)
        time.sleep(0.1)
        GPIO.output(23,True)
        time.sleep(0.1)
        GPIO.output(23,False)
        time.sleep(0.1)
        GPIO.output(23,True)
        time.sleep(0.1)
        GPIO.output(23,False)
	time.sleep(0.1)
	GPIO.output(23,True)
	time.sleep(0.1)
	GPIO.output(23,False)
        time.sleep(5)
 print "done!!"
 GPIO.cleanup()
Blink()
