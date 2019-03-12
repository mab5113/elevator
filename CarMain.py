#!/usr/bin/python3

#runs setup programs
 
# Import required libraries
from CarManager import CarManager
from CarLampMonitor import CarLampMonitor
import udpListener
	
def CarMain(carID,ipAddress):
	print ('Starting CarMain')
	CarLampMonitor()
	udpListener()
	CarManager()
