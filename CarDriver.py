#!/usr/bin/python

import time
import RPi.GPIO as GPIO
from CarMotorDriver import CarMotorDriver

def CarDriver(command,moveSteps,waitTime):
	# Use BCM GPIO references
	# instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
		
	if command == 'reset':
		rv = CarMotorDriver(-99999,waitTime)
		print('CarDriver CarMotorDriver: ', rv)
		CarCurrentFloor=1
		CarCurrentDirection=1
		return rv
	elif command=='move':
		rv = CarMotorDriver(moveSteps,waitTime)
		print('CarDriver CarMotorDriver: ', rv)

	else:
	
		print("CarDriver: ", moveSteps, waitTime)
		stepPos
		Direction = -1
		#waitTime = .004
		StepCounter = 0
		currentStep = 0
	
		#set up top and bottom floor limit switches
		GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(8,GPIO.IN, pull_up_down=GPIO.PUD_UP)
		if not GPIO.input(7):
			print("top Limit closed")
			stepDir = -1
		
		elif not GPIO.input(8):
			print("bottom limit closed")
			stepDir = 1
	
		CarMotorDriver(moveSteps, waitTime)


	
	
