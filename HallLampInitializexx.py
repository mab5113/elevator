# TODO
#   Describe this Module
#   Use pin names in config - no magic pin numbers

import time
import RPi.GPIO as GPIO
from HallLampCallBack import HallLampCallBack

def HallLampInitialize():

	print ('HallLampInitialize: initialize')
	# Use BCM GPIO references instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
		
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(12,GPIO.OUT)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(14,GPIO.OUT)
	GPIO.setup(15,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)
	GPIO.setup(17,GPIO.OUT)
	GPIO.setup(18,GPIO.OUT)

	GPIO.output(11,False)
	GPIO.output(12,False)
	GPIO.output(13,False)
	GPIO.output(14,False)
	GPIO.output(15,False)
	GPIO.output(16,False)
	GPIO.output(17,False)
	GPIO.output(18,False)
	time.sleep(2)
	GPIO.output(11,True)
	GPIO.output(12,True)
	GPIO.output(13,True)
	GPIO.output(14,True)
	GPIO.output(15,True)
	GPIO.output(16,True)
	GPIO.output(17,True)
	GPIO.output(18,True)

