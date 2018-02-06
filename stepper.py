import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

GPIO.setup(23,GPIO.LOW)

for i in range(0,30):
	GPIO.output(18,GPIO.HIGH)
	print('High')
	time.sleep(.4)

	GPIO.output(18, GPIO.LOW)
	print('LOW')
	time.sleep(.4)


