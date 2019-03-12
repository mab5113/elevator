import RPi.GPIO as GPIO

def CarLampInitialize():

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
	
	#Turn on the Car button/lamps
	GPIO.output(19,False)
	GPIO.output(20,False)
	GPIO.output(21,False)
	GPIO.output(22,False)
	GPIO.output(23,False)

	time.sleep(2)

	#Turn off the Car button/lamps
	GPIO.output(19,True)
	GPIO.output(20,True)
	GPIO.output(21,True)
	GPIO.output(22,True)
	GPIO.output(23,True)
	
