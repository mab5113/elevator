import time
import RPi.GPIO as GPIO
	
class CarMotorDriver():
	stepDelayTime = .004
	currentPosition = 0
	grandTotalSteps = 0
	Seq = [[1,0,0,1], [1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1]]
	SeqLength = len(Seq)

	#def __init__(self): 
	# instance variables unique to each instance
	
	# Define H-bridge sequence in manufacturers datasheet
	#  Notice that from step to step, only one bit changes
	
	# Use BCM GPIO references
	# instead of physical pin numbers
	GPIO.setmode(GPIO.BCM)
	
	#set up top and bottom floor limit switches
	GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(8,GPIO.IN, pull_up_down=GPIO.PUD_UP)

	# Define GPIO signals to use
	# Physical pins 5, 7, 29, 31
	# GPIO3, GPIO4, GPIO5, GPIO6
	stepPins = [3,4,5,6]
							   
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
			if not GPIO.input(7):
				print("bottom limit")
				return 0
		else:
			stepDir = -1
			if not GPIO.input(8) :
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

