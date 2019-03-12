#!/usr/bin/python3

# imports and runs the different classes used to move the car and light up the lamps
# imports the CarLampMonitor Class from CarLampMonitor.py
# imports the CarManager class from ClassManager.py
 
# Import required libraries
# import config
# import time

from CarManager import CarManager
from CarLampMonitor import CarLampMonitor
from udpListener import udpListener
	
def CarMain(carID,ipAddress):
	print ('Starting CarMain')
	CarLampMonitor()
	udpListener()
	CarManager()
