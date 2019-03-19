#!/usr/bin/python
# TODO:
#   add comments at top of this module the describe the purpose of this module
#   Describe reason for the StepperDriverClass
#   Add recommendations for identifier names


import random
import time
import config
import RPi.GPIO as GPIO
#import CarDoorManager from CarDoorManager
#from udpSend import udpSend

from StepperDriverClass import StepperDriverClass
from CarLampManager import CarLampManager

def send(message):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.sendto(message.encode(), ("192.168.254.81", 5005))

def CarManager(id):
	
	#Create an instance of the stepper motor driver
	Car=StepperDriverClass(id, [6,5,4,3], 7, 8 )

	#stepPos = 0
		
	Car.move2Position(-10000)	#???
	CurrentFloor=1
	CurrentDirection = 1
	CurrentStepPosition = 0
	time.sleep(.5)

	#Setting parameters for directions, height of elevator, and initial position
	up = 1
	down = -1
	topFloor = 5
	floor = 1
	direction = 1

	print ('CarManager: Starting main loop')

	while True:
		# Poll the floor calls continuously
		
		# TODO:  convert this code to process without if statements
		
		if config.CarFloorStopList[floor] == 1:
			config.CarFloorStopList[floor] = 0
			print ('CarManager: Moving to floor ', floor)
			
			if floor == 1:
				Car.move2Position(-1000)
				#send('moving to floor ' + str(floor))
          
			elif floor == 2:
				Car.move2Position(config.CarTopPosition[1]/4)
				#send('moving to floor ' + str(floor))
  
			elif floor == 3:
				Car.move2Position(config.CarTopPosition[1] / 4 * 2)
				#send('moving to floor ' + str(floor))
  
			elif floor == 4:
				Car.move2Position(config.CarTopPosition[1] / 4 * 3)
				#send('moving to floor ' + str(floor))
  

			elif floor == 5:
				Car.move2Position(100000)
				#send('moving to floor ' + str(floor))
				
  			CarDoorManager()
			print ('CarManager: Arrived floor ', floor)
			CurrentStatus='stopped'
			CarLampManager(floor, 0)
		time.sleep(.5)

		
		# config.CarFloorStopList[0] = config.CarFloorStopList[0] + 1
		# print (config.CarFloorStopList)

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
		config.CarFloorStopList[f] = 1
		CarLampManager(f, 1)
		time.sleep(1)
		print (config.CarFloorStopList)

	while True:  # making a loop
		if keyboard.is_pressed('q'):  # if key 'q' is pressed 
			print('You Pressed A Key!')
			break  # finishing the loop
		time.sleep(2)
		print('No key Pressed!')
		
