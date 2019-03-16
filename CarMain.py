#!/usr/bin/python3

#runs setup programs
 
# Import required libraries
from CarManager import CarManager
from CarLampInitialize import CarLampInitialize
from CarButtonInitialize import CarButtonInitialize
from udpListener import *
	
def CarMain(id):
	print ('Starting CarMain')
	CarButtonInitialize(id)
	CarLampInitialize(id)
	udpListenerMain(id)
	CarManager(id)
