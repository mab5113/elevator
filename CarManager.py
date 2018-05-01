#!/usr/bin/python

import time
import config
import RPi.GPIO as GPIO

from StepperDriverClass import StepperDriverClass
from CarLampManager import CarLampManager

def CarManager(command,moveSteps,waitTime):


	Car=StepperDriverClass()
	
	stepPos = 0
		
	Car.DoSteps(-10000)
	CarCurrentFloor=1
	CarCurrentDirection = 1



	while True:
		print(config.FloorStopList)
		StopCount = 0
		for floor in range (CarCurrentFloor, 5):
			if config.FloorStopList[1] == 1:
				StopCount +=1
		if StopCount > 0:
			CarCurrentDirection = 1
		else:
			for floor in range (CarCurrentFloor, 0):
				CarCurrentDirection = -1


		if config.FloorStopList[1] == 1:
			Car.DoSteps(2200 * CarCurrentDirection)
			CarCurrentFloor=1
			CarCurrentSteps= 2200
			config.FloorStopList[1] = 0
			CarCurrentStatus='stopped'
			CarLampManager(CarCurrentFloor, 0)

		if config.FloorStopList[2] == 1:
			Car.DoSteps(2200 * CarCurrentDirection)
			CarCurrentFloor=2
			CarCurrentSteps= 3500
			CarLampManager(CarCurrentFloor, 0)
			config.FloorStopList[2] = 0
			CarCurrentStatus='stopped'

		if config.FloorStopList[3] == 1:
			Car.DoSteps(2200 * CarCurrentDirection)
			CarCurrentFloor=3
			CarCurrentSteps= 4500
			config.FloorStopList[3] = 0
			CarCurrentStatus='stopped'
			CarLampManager(CarCurrentFloor, 0)

		if config.FloorStopList[4] == 1:
			Car.DoSteps(2200 * CarCurrentDirection)
			CarCurrentFloor=4
			CarCurrentSteps= 5500
			config.FloorStopList[4] = 0
			CarCurrentStatus='stopped'
			CarLampManager(CarCurrentFloor, 0)

		if config.FloorStopList[5] == 1:
			Car.DoSteps(6500 * CarCurrentDirection)
			CarCurrentFloor=5
			CarCurrentSteps= 6500
			config.FloorStopList[5] = 0
			CarCurrentStatus='stopped'
			CarLampManager(CarCurrentFloor, 0)


		time.sleep(1)
