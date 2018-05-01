import config
import os
import RPi.GPIO as GPIO
from CarMain import CarMain

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

#Check device ID
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25,GPIO.IN, pull_up_down=GPIO.PUD_UP)



if not GPIO.input(24):
	id1=0
else:
	id1=1

if not GPIO.input(25):
	id2=0
else:
	id2=1


id= id1 + id2 * 2

print(id1,id2)

if id == 0:
	ipAddress='10.81.104.120/24'
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')

	HallMain(id,ipAddress)
elif id == 1:
	ipAddress='10.81.104.121/24'
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	CarMain(id,ipAddress)

elif id == 2:
	ipAddress='10.81.104.122/24'
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	CarMain(id,ipAddress)

elif id == 3:
	ipAddress='10.81.104.123/24'
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 ' + ipAddress)
	os.system('sudo ifconfig eth0 up')
	CarMain(id,ipAddress)


#def CarStartUp():
