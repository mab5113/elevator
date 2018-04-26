#!/usr/bin/python

import time
import config
import RPi.GPIO as GPIO
from CarMotorDriver import CarMotorDriver


def CarDriver(command,moveSteps,waitTime):

carDriver= CarMotorDriver()
	

	if command == 'reset':
		rv = carDriver.DoSteps(-99999)
		print('CarDriver CarMotorDriver: ', rv)
		CarCurrentFloor=1
		CarCurrentDirection=1
		return rv
	elif command=='move':
		rv = carDriver.DoSteps(moveSteps)
		print('CarDriver CarMotorDriver: ', rv)

	else:
		CarMotorDriver(moveSteps)


	
	
