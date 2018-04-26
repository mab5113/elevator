import time
import RPi.GPIO as GPIO
	
class CarDoorDriver():
	stepDelayTime = .004
	currentStepPosition = 0
	grandTotalSteps = 0
	
	# Define H-bridge sequence in manufacturers datasheet
	#  Notice that from step to step, only one bit changes	
	Seq = [[1,0,0,1], [1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1]]
	SeqLength = len(Seq)

	#def __init__(self): 
	# instance variables unique to each instance
	
	# Use BCM GPIO references
	# instead of physical pin numbers
	GPIO.setmode(GPIO.BCM)
	
	#set up top and bottom floor limit switches
	GPIO.setup(8,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)

	# Define GPIO signals to use
	# Physical pins 21,19,23,32
	# GPIO9, GPIO10, GPIO11, GPIO12
	stepPins = [9,10,11,12]
							   
	# Set all pins as output
	for pin in stepPins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)
		
		
	def DoSteps(moveSteps):
		totalSteps = 0
		
		# Allow for hystersis of the limit switches
		#  It will take n steps for the limit switch to open
		LimitSwitchHystersis = 300

		if moveSteps < 0:
			stepDir = 1
			moveSteps = abs(moveSteps)
			if not GPIO.input(8):
				print("bottom limit")
				return 0
		else:
			stepDir = -1
			if not GPIO.input(13) :
				print("top limit")
				return 999999
				
		while totalSteps < moveSteps:
			StepCounter =0
			# This where all the action happens. There are 8 microsteps per step
			for pin in range(0, 4):
				xpin = StepPins[pin]
				if Seq[StepCounter][pin]=0:
					GPIO.output(xpin, False)
				else:
					GPIO.output(xpin, True)
					
	 
			# Notice that stepcounter will decrease if stepDir is negative
			StepCounter += stepDir
			
			# When at the end of the step sequence start again
			if (StepCounter>=StepCount):
				self.SeqLength = 0
			
			if (StepCounter<0):
				self.SeqLength = StepCount + self.stepDir
				
			if self.stepDir == 1:
				currentStepPosition -= 1
			else:
				currentStepPosition +=-1
				
			self.totalSteps += 1		# completed one motor step, count it
			self.grandTotalSteps += 1
				
		
			if not GPIO.input(7) and totalSteps > LimitSwitchHystersis:
				print("bottom limit")
				return 0
			
			if not GPIO.input(8) and totalSteps > LimitSwitchHystersis:
				print("top limit")
				return self.totalSteps
				
			# Wait before doing the next step
			time.sleep(self.stepDelayTime)

		Return self.totalSteps

