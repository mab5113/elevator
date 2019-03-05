#!/usr/bin/python3

#ToDO: add description of this module
#  
 
# Import required libraries
# import config
# import time

from CarManager import CarManager
from CarLampMonitor import CarLampMonitor
import udpListener
	
def CarMain(carID,ipAddress):
	CarLampMonitor()
	udpListener()
	CarManager()
