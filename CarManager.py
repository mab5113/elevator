#!/usr/bin/python

import time
import config
import RPi.GPIO as GPIO

from StepperDriverClass import StepperDriverClass
from CarLampManager import CarLampManager

def CarManager():

	Car=StepperDriverClass()
	
	stepPos = 0
		
	Car.move2Position(-10000)
	CurrentFloor=1
	CurrentDirection = 1
	CurrentStepPosition = 0
	time.sleep(.5)

	print ('CarManager: Starting main loop')
	while True:
		# print(config.FloorStopList)
		
		if config.FloorStopList[1] == 1:
			CurrentFloor=1
			config.FloorStopList[CurrentFloor] = 0
			print ('CarManager: Moving to floor 1')
			Car.move2Position(-1000)
			print ('CarManager: Arrived floor 1')
			CurrentStatus='stopped'
			CarLampManager(CurrentFloor, 0)
			time.sleep(5)

		if config.FloorStopList[2] == 1:
			CurrentFloor=2
			config.FloorStopList[CurrentFloor] = 0
			print ('CarManager: Moving to floor 2')
			Car.move2Position(config.CarTopPosition/4)
			print ('CarManager: Arrived floor 2')
			CurrentStatus='stopped'
			CarLampManager(CurrentFloor, 0)
			time.sleep(5)

		if config.FloorStopList[3] == 1:
			CurrentFloor=3
			config.FloorStopList[CurrentFloor] = 0
			print ('CarManager: Moving to floor 3')
			Car.move2Position(config.CarTopPosition/4 *2
			print ('CarManager: Arrived floor 3')
			CurrentStatus='stopped'
			CarLampManager(CurrentFloor, 0)
			time.sleep(5)
			
		if config.FloorStopList[4] == 1:
			CurrentFloor=4
			config.FloorStopList[CurrentFloor] = 0
			print ('CarManager: Moving to floor 4')
			Car.move2Position(config.CarTopPosition/4 * 3)
			print ('CarManager: Arrived floor 4')
			CurrentStatus='stopped'
			CarLampManager(CurrentFloor, 0)
			time.sleep(5)

		if config.FloorStopList[5] == 1:
			print ('CarManager: Moving to floor 5')
			Car.move2Position(100000)
			print ('CarManager: Arrived floor 5')
			CurrentFloor=5
			config.FloorStopList[5] = 0
			CurrentStatus='stopped'
			CarLampManager(CurrentFloor, 0)
			time.sleep(5)

		#print('Current Step Position', config.CarCurrentStepPosition)

		time.sleep(.5)
