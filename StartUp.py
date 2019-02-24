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

#Check device ID
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25,GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Read IO port if find ID
if not GPIO.input(24):
	id1=1
else:
	id1=0

if not GPIO.input(25):
	id2=1
else:
	id2=0


#Convert inputs  to a binary number
id= id1 + id2 * 2

print('ID: ',id, id1,id2)



if id == 0:
	ipAddress='10.81.104.120/24'
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	print('Hallway ID found')
	HallMain(id,ipAddress)

elif id == 1:
	ipAddress='10.81.104.121/24'
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	print('Car Main 1 ID found')
	CarMain(id,ipAddress)

elif id == 2:
	ipAddress='10.81.104.122/24'
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	print('Car Main 2 ID found')
	CarMain(id,ipAddress)

elif id == 3:
	ipAddress='10.81.104.123/24'
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	CarMain(id,ipAddress)


#def CarStartUp():
