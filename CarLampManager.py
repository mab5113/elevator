import time
import RPi.GPIO as GPIO
import config

def CarLampManager(floor,status):  

	# Use BCM GPIO references
	# instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.output(19,True)
	GPIO.output(20,True)
	GPIO.output(21,True)
	GPIO.output(22,True)
	GPIO.output(23,True)

	if floor == 1:
		GPIO.output(14,True)
		config.FloorStopList[floor]=status

	if floor == 2:
		GPIO.output(15,True)
		config.FloorStopList[floor]=status

	if floor == 3:
		GPIO.output(16,True)
		config.FloorStopList[floor]=status

	if floor == 4:
		GPIO.output(17,True)
		config.FloorStopList[floor]=status

	if floor == 5:
		GPIO.output(18,True)
		config.FloorStopList[floor]=status
