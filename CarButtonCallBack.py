#!/usr/bin/python3
# callback handler for car button press 

#import time
import RPi.GPIO as GPIO
import config

def CarButtonCallBack(channel):  
	# All button presses in the car go here to be handled
	
	print ("Button press detected on : ",channel)  
	
	# Use BCM GPIO references instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)	
	
	
	"""
	# Changed to index lookup
	floor = 0
	if   channel == 14: floor=1			
	elif channel == 15: floor=2
	elif channel == 16: floor=3
	elif channel == 17: floor=4
	elif channel == 18: floor=5
	"""
	
	floor = config.CarLampsPins.index(channel)
	print ('CarButtonCallBack: Floor -->', floor)
	print ('CarButtonCallBack: old CarFloorStopList: ', config.FloorStopList)
	
	# If floor lamp indicator in car is off, Turn on and add set list to stop at floor
	#If floor lamp indicator in car is on, Turn it off and remove from list 
	lampPin=config.CarLampsPins[floor]
	
	if config.CarFloorStopList[floor] == 0:
		config.CarFloorStopList[floor] = 1
		GPIO.output(lampPin,False)
	else:
		config.CarFloorStopList[floor] = 0
		GPIO.output(lampPin, True)
	
	print ('CarButtonCallBack: New CarFloorStopList: ', config.FloorStopList)
