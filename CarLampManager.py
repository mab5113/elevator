import time
import RPi.GPIO as GPIO
import config

def CarLampManager(floor,status):  

	# Use BCM GPIO references
	# instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(19,GPIO.OUT)
	GPIO.setup(20,GPIO.OUT)
	GPIO.setup(21,GPIO.OUT)
	GPIO.setup(22,GPIO.OUT)
	GPIO.setup(23,GPIO.OUT)

	
	if floor == 1:
		GPIO.output(19,True)
		config.FloorStopList[floor]=status

	if floor == 2:
		GPIO.output(20,True)
		config.FloorStopList[floor]=status

	if floor == 3:
		GPIO.output(21,True)
		config.FloorStopList[floor]=status

	if floor == 4:
		GPIO.output(22,True)
		config.FloorStopList[floor]=status

	if floor == 5:
		GPIO.output(23,True)
		config.FloorStopList[floor]=status
