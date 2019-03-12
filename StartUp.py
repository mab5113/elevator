#!/usr/bin/python3
#StartUp.py 
# Determines the role of this RPi by reading jumpers on two inputs

import config
import os
import RPi.GPIO as GPIO
from CarMain import CarMain

IDPin1=24
IDPin2=25

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Setup RPi device I/O
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Read IO ports if find ID
id1in = GPIO.input(24)
id2in = GPIO.input(25)

# Switch closure will pull the port to ground (0 Volts)
#  This same as logic false

print ('StartUp: id1in: ', id1in)
print ('StartUp: id1in: ', id2in)

# Need to change switch closure to True using not
if not GPIO.input(24): id1=1
else: 	id1=0

if not GPIO.input(25): 	id2=1
else: 			id2=0

#Convert inputs  to a binary number
id= id1 + id2 * 2

print(' ID1:', id1, '  ID2:', id2, '   ID:', id)

print ('StartUp: floorStopList; ', config.FloorStopList)

if id == 0:
	ipAddress=config.IpHall
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	print ('')
	print('StartUP: Hallway ID found --> starting HallMain()')
	#HallMain()

elif id == 1:
	ipAddress= config.IpCar1
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	print ('')
	print('StartUp: Car Main 1 ID found --> Starting CarMain()')
	CarMain(id,ipAddress)

	#Car ID and ip address are passed as arguments to car main function

elif id == 2:
	ipAddress=config.IpCar2
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	print('')
	print('StartUp: Car Main 2 ID found --> Starting CarMain()')
	#CarMain(id,ipAddress)

elif id == 3:
	ipAddress=IpCar3
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	print ('')
	print('StartUp: Car Main 2 ID found --> Starting CarMain()')
	#CarMain(id,ipAddress)
	
