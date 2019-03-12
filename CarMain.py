#!/usr/bin/python3

#runs setup programs
 
# Import required libraries
from CarManager import CarManager
from CarLampInitialize import CarLampInitialize
from CarButtonInitialize import CarButtonInitialize
from udpListener import *
	
def CarMain(carID,ipAddress):
	print ('Starting CarMain')
	CarButtonIntialize()
	CarLampInitialize()
	udpListenerMain()
	CarManager()
