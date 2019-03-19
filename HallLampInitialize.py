# TODO
#   Describe this Module
#   Use pin names in config - no magic pin numbers

import RPi.GPIO as GPIO
import time

def HallLampInitialize(id):

	print ('HallLampInitialize: initialize')
	# Use BCM GPIO references instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	HallDownLampPinID = [11,12,13,14] #No floor 1 Down
	HallUpLampPinID   = [15,16,17,18] #No floor 5 Up
	
	#Down Lamps setup
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(12,GPIO.OUT)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(14,GPIO.OUT)
	
	#Up Lamps setup
	GPIO.setup(15,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)
	GPIO.setup(17,GPIO.OUT)
	GPIO.setup(18,GPIO.OUT)

	# Turn on the Down Lamps by pulling the output to ground
	GPIO.output(11,False)
	GPIO.output(12,False)
	GPIO.output(13,False)
	GPIO.output(14,False)
	
	# Turn on the Up Lamps
	GPIO.output(15,False)
	GPIO.output(16,False)
	GPIO.output(17,False)
	GPIO.output(18,False)
	
	time.sleep(2)
	
	# Turn off the Down Lamps
	GPIO.output(11,True)
	GPIO.output(12,True)
	GPIO.output(13,True)
	GPIO.output(14,True)
	
	# Turn off the Down Lamps
	GPIO.output(15,True)
	GPIO.output(16,True)
	GPIO.output(17,True)
	GPIO.output(18,True)

