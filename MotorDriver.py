import sys
import time
import RPi.GPIO as GPIO
	
def MotorDriver(moveSteps,waitTime):
	print ('MotorDriver: ', moveSteps,waitTime)
	if moveSteps < 0:
		StepDir = 1
		moveSteps = abs(moveSteps)
	else:
		StepDir = -1

	print (StepDir)

	time.sleep(3)

	# Use BCM GPIO references
	# instead of physical pin numbers
	GPIO.setmode(GPIO.BCM)
	
	# Define GPIO signals to use
	# Physical pins 5, 7, 29, 31
	# GPIO3, GPIO4, GPIO5, GPIO6
	StepPins = [3,4,5,6]
	                           
	# Set all pins as output
	for pin in StepPins:
		print "Setup pins"
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)
	 
	#set up top and bottom floor limit switches
	print ('set limit switch IO')
	GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(8,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	totalSteps = 0
	
	# Define  sequence in manufacturers datasheet
	Seq = [[1,0,0,1],
		[1,0,0,0],
		[1,1,0,0],
		[0,1,0,0],
		[0,1,1,0],
		[0,0,1,0],
		[0,0,1,1],
[		0,0,0,1]]
	
       
	StepCount = len(Seq)
	
	
	WaitTime = waitTime
	 
	# Initialise variables
	StepCounter = 0
	 
	# Start main loop=============================
	while totalSteps < moveSteps:
		print StepCounter,
		print Seq[StepCounter]
		
		for pin in range(0, 4):
			xpin = StepPins[pin]
			if Seq[StepCounter][pin]!=0:
				GPIO.output(xpin, True)
			else:
				GPIO.output(xpin, False)
	 
		StepCounter += StepDir
		
		# If we reach the end of the sequence
		# start again
		if (StepCounter>=StepCount):
			StepCounter = 0
		
		if (StepCounter<0):
			StepCounter = StepCount+StepDir
		
		# Wait before moving on
		time.sleep(WaitTime)
	
		totalSteps += 1
		print(totalSteps)
		
		if not GPIO.input(7) and totalSteps > 300:
			print("bottom limit")
			return 0
		
		if not GPIO.input(8) and totalSteps > 300:
			print("top limit")
			return totalSteps
