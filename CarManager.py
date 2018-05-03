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
	CarCurrentFloor=1
	CarCurrentDirection = 1
	CarCurrentStepPosition = 0
	time.sleep(1)

	while True:
		# print(config.FloorStopList)
		
		if config.FloorStopList[1] == 1:
			Car.move2Position(-1000)
			CarCurrentFloor=1
			config.FloorStopList[1] = 0
			CarCurrentStatus='stopped'
			CarLampManager(CarCurrentFloor, 0)

		if config.FloorStopList[2] == 1:
			Car.move2Position(config.CarTopPosition/4)
			CarCurrentFloor=2
			CarLampManager(CarCurrentFloor, 0)
			config.FloorStopList[2] = 0
			CarCurrentStatus='stopped'

		if config.FloorStopList[3] == 1:
			Car.move2Position(config.CarTopPosition/4 *2)
			CarCurrentFloor=3
			config.FloorStopList[3] = 0
			CarCurrentStatus='stopped'
			CarLampManager(CarCurrentFloor, 0)

		if config.FloorStopList[4] == 1:
			Car.move2Position(config.CarTopPosition/4 * 3)
			CarCurrentFloor=4
			config.FloorStopList[4] = 0
			CarCurrentStatus='stopped'
			CarLampManager(CarCurrentFloor, 0)

		if config.FloorStopList[5] == 1:
			Car.move2Position(100000)
			CarCurrentFloor=5
			config.FloorStopList[5] = 0
			CarCurrentStatus='stopped'
			CarLampManager(CarCurrentFloor, 0)


		#print('Current Step Position', config.CarCurrentStepPosition)

		time.sleep(.5)
