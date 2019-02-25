import time
import RPi.GPIO as GPIO
import config

def CarLampManager(floor,status):  

	# Use BCM GPIO references
	# instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	
	carFloorLamp1= 19
	carFloorLamp2 = 20
	carFloorLamp3 = 21
	carFloorLamp4 = 22
	carFloorLamp5 = 23
	
	#Set RPi output such that a True (High) outputs +5V to pin
	#  the Led-resistor is connected to ground to compete the circut
	#  and turn on the LED
	
	GPIO.setmode(GPIO.BCM)		# Use pin numbers, not GPIO numbers
	GPIO.setwarnings(False)
	GPIO.setup(carFloorLamp1,GPIO.OUT)
	GPIO.setup(carFloorLamp2,GPIO.OUT)
	GPIO.setup(carFloorLamp3,GPIO.OUT)
	GPIO.setup(carFloorLamp4,GPIO.OUT)
	GPIO.setup(carFloorLamp5,GPIO.OUT)

	
	if floor == 1:
		GPIO.output(carFloorLamp1,True)
		#config.FloorStopList[floor]=status

	if floor == 2:
		GPIO.output(carFloorLamp2,True)
		#config.FloorStopList[floor]=status

	if floor == 3:
		GPIO.output(carFloorLamp3,True)
		#config.FloorStopList[floor]=status

	if floor == 4:
		GPIO.output(carFloorLamp4,True)
		#config.FloorStopList[floor]=status

	if floor == 5:
		GPIO.output(carFloorLamp5,True)
		#config.FloorStopList[floor]=status
