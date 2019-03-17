#!/usr/bin/python3
#StartUp.py 
# Determines the role of this RPi by reading jumpers on two inputs

import config
import os
import RPi.GPIO as GPIO
from CarInitialize import CarInitialize
from HallInitialize import HallInitialize

IDPin1=24
IDPin2=25

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Setup RPi device I/O
GPIO.setup(IDPin1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IDPin2,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Read IO ports if find ID
id1in = GPIO.input(IDPin1)
id2in = GPIO.input(IDPin2)

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

<<<<<<< HEAD
print ()
print(' ID1:', id1, '  ID2:', id2, '   ID:', id)
=======
print(' ID:', id)
>>>>>>> 8c387b4db614ec251c6c9d2eaa45773b1fe04ae3

print ('StartUp: floorStopList; ', config.FloorStopList)
print ()

if id == 0:
	#Hallway
	ipAddress=config.IpHall
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	print ('')
	print('StartUP: Hallway ID found --> starting HallMain()')
	HallInitialize(id)

elif id == 1:
	# Car 1
	ipAddress= config.IpCar1
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	print ('')
	print('StartUp: Car Main 1 ID found --> Starting CarMain()')
	CarInitialize(id)

	#Car ID and ip address are passed as arguments to car main function

elif id == 2:
	# Car 2
	ipAddress=config.IpCar2
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	print('')
	print('StartUp: Car Main 2 ID found --> Starting CarMain()')
<<<<<<< HEAD
	CarMain(id,ipAddress)
=======
	CarInitialize(id)
>>>>>>> 8c387b4db614ec251c6c9d2eaa45773b1fe04ae3

elif id == 3:
	# Use to be determined
	ipAddress=IpCar3
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	print ('')
	print('StartUp: Car Main 2 ID found --> Starting CarMain()')
	#CarInitialize(id)
	
