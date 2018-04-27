#!/usr/bin/python3
 
# Import required libraries

import time

from CarDriver import CarDriver
from CarMotorDriver import CarMotorDriver
from CarLampDriver import CarLampDriver
import config
	
def main():
	CarLampDriver('initialize',0,0)

	car=
	
	stepPos = 0
	 
	# Use BCM GPIO references
	# instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	
	#GPIO.setmode(GPIO.BCM)
	#GPIO.setwarnings(False)


	print(config.FloorStopList)
	CarDriver('reset',0,.004)

	while True:
		if config.FloorStopList[2] == 1:
			CarDriver('move',2200,.004)
			CarCurrentFloor=1
			CarCurrentSteps= 2200
			CarCurrentStatus='stopped'

		if config.FloorStopList[3] == 1:
			CarDriver('move',2200,.004)
			CarCurrentFloor=1
			CarCurrentSteps= 3500
			CarCurrentStatus='stopped'


		time.sleep(.4)

	
	
main()
