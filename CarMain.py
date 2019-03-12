#!/usr/bin/python3

#runs setup programs
 
# Import required libraries
from CarManager import CarManager
from CarLampMonitor import CarLampMonitor
from udpListener import *
	
def CarMain(carID,ipAddress):
	print ('Starting CarMain')
	CarLampMonitor()
	main()
	CarManager()
