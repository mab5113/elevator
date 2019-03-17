#!/usr/bin/python3

#runs setup programs
 
# Import required libraries
from CarManager import CarManager
from CarLampInitialize import CarLampInitialize
from CarButtonInitialize import CarButtonInitialize
from udpListener import *
	
def CarInitialize(id):
	print ('Starting CarInitialize for car #', id)
	
	#TODO: change to simple loop (for any list length)
	config.CarFloorStopList[0] = 0
	config.CarFloorStopList[1] = 0
	config.CarFloorStopList[2] = 0
	config.CarFloorStopList[3] = 0
	config.CarFloorStopList[4] = 0
	config.CarFloorStopList[5] = 0
	
	CarButtonInitialize(id)
	CarLampInitialize(id)
	#udpListenerMain(id)
	CarManager(id)

	print ('Starting CarInitialize for car #', id)
