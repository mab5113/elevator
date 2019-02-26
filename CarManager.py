#!/usr/bin/python
# TODO:
#   add comments at top of this module the describe the purpose of this module
#   Describe reason for the StepperDriverClass
#   Add recommendations for identifier names

import random
import time
import config
import RPi.GPIO as GPIO

from StepperDriverClass import StepperDriverClass
from CarLampManager import CarLampManager

def CarManager():

	Car=StepperDriverClass()
	
	stepPos = 0
		
	Car.move2Position(-10000)	#???
	CurrentFloor=1
	CurrentDirection = 1
	CurrentStepPosition = 0
	time.sleep(.5)

	up = 1
	down = -1
	topFloor = 5
	floor=1
	direction=1

	config.FloorStopList[1] = 0
	config.FloorStopList[2] = 0
	config.FloorStopList[3] = 0
	config.FloorStopList[4] = 0
	config.FloorStopList[5] = 0

	print ('CarManager: Starting main loop')

	while True:
		# TODO:  convert this code to process without if statements
		
		if config.FloorStopList[floor] == 1:
			config.FloorStopList[floor] = 0
			print ('CarManager: Moving to floor ', floor)
			
			if floor == 1:
				Car.move2Position(-1000)
			                  
			elif floor == 2:
                                Car.move2Position(config.CarTopPosition/4)

			elif floor == 3:
				Car.move2Position(config.CarTopPosition / 4 * 2)

			elif floor == 4:
				Car.move2Position(config.CarTopPosition / 4 * 3)


			elif floor == 5:
				Car.move2Position(100000)

			print ('CarManager: Arrived floor ', floor)
			CurrentStatus='stopped'
			CarLampManager(floor, 0)
			time.sleep(5)

		
		config.FloorStopList[0] = config.FloorStopList[0] + 1
		print (config.FloorStopList)

		# TODO: Explain this code
		floor = floor + direction
		if floor == topFloor + 1:
			direction = down
			floor = topFloor - 2
		if floor ==0:
			direction = up
			floor = 2

                print (floor)
		
		#code to exercise the elevator
		#f = random.randint(1,5)
		#config.FloorStopList[f] = 1
		#CarLampManager(f, 1)
