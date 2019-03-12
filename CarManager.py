#!/usr/bin/python
# TODO:
#   add comments at top of this module the describe the purpose of this module
#   Describe reason for the StepperDriverClass
#   Add recommendations for identifier names

import socket
import random
import time
import config
import RPi.GPIO as GPIO
# import keyboard  # using module keyboard

from StepperDriverClass import StepperDriverClass
from CarLampManager import CarLampManager

def send(message):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.sendto(message.encode(), ("192.168.254.81", 5005))


def CarManager():

	Car=StepperDriverClass()
	
	stepPos = 0
		
	Car.move2Position(-10000)	#???
	CurrentFloor=1
	CurrentDirection = 1
	CurrentStepPosition = 0
	time.sleep(.5)

	#Setting parameters for directions, height of elevator, and initial position
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
				send('moving to floor ', floor
          
			elif floor == 2:
				Car.move2Position(config.CarTopPosition[1]/4)
				send('moving to floor ', floor)
  
			elif floor == 3:
				Car.move2Position(config.CarTopPosition[1] / 4 * 2)
				send('moving to floor ', floor)
  
			elif floor == 4:
				Car.move2Position(config.CarTopPosition[1] / 4 * 3)
				send('moving to floor ', floor)
  

			elif floor == 5:
				Car.move2Position(100000)
				send('moving to floor ', floor)
  
			print ('CarManager: Arrived floor ', floor)
			CurrentStatus='stopped'
			CarLampManager(floor, 0)
		time.sleep(.5)

		
		# config.FloorStopList[0] = config.FloorStopList[0] + 1
		# print (config.FloorStopList)

		# floor will start at 0, this makes it so the first floor will be 1, etc
		floor = floor + direction
		# floor = floor +1 
		if floor == topFloor +1:
			direction = down
			floor = topFloor + direction
		if floor ==0:
			direction = up
			floor =  floor + direction

		print ('CarManager: ', floor)

		#code to exercise the elevator
		f = random.randint(1,5)
		config.FloorStopList[f] = 1
		CarLampManager(f, 1)
		time.sleep(1)
		print (config.FloorStopList)

	while True:  # making a loop
		if keyboard.is_pressed('q'):  # if key 'q' is pressed 
			print('You Pressed A Key!')
			break  # finishing the loop
		time.sleep(2)
		print('No key Pressed!')


