import time
import RPi.GPIO as GPIO
	
class CarDoorDriver():
	stepDelayTime = .004
	currentCarPosition = 0
	LifeTimeTotalSteps = 0
	CarStatus=""
		
	# Allow for hystersis of the limit switches
	#  It will take n steps for the limit switch to open
	LimitSwitchHystersis = 300

	# Define H-bridge sequence in manufacturers datasheet
	#  Notice that from step to step, only one bit changes	
	Seq = [[1,0,0,1], [1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1]]
	SeqLength = len(Seq)

	#def __init__(self): 
		# instance variables unique to each instance
		pass
	
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

	# Set all H-Bridge Raspberry pins as output
	for pin in stepPins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)

	def SetstepDelayTime(stepDelay):
		self.stepDelayTime = self.stepDelay
	
	def GetcurrentCarPosition():
		return self.currentCarPosition 
		
	def IsAtBottom():
		if GPIO.input(7):
		return False

	def IsAtTop():
		if GPIO.input(8):
		return False
		

	def DoSteps(moveSteps):
		stepsCompleted = 0
		
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
				return self.currentCarPosition
				
		while stepsCompleted < moveSteps:
			StepCounter = 0

			# This where all the action happens. 
			# There are 4 pins
			for pin in range(0, 4):
				xpin = StepPins[pin]
				if Seq[StepCounter][pin]=0:
					GPIO.output(xpin, False)
				else:
					GPIO.output(xpin, True)
 
			# Notice that stepcounter will decrease if stepDir is negative
			self.StepCounter += self.stepDir
			
			# When at the end of the step sequence start again
			if (StepCounter>=StepCount):
				self.SeqLength = 0
			
			if (StepCounter<0):
				self.SeqLength = StepCount + self.stepDir
				
			self.currentCarPosition += stepDir
						
			stepsCompleted += 1		# completed one motor step, count it
			self.LifeTimeTotalSteps += 1	
		
			if not GPIO.input(7):
				self.currentCarPosition = 0
				self.carStatus = 'bottom'
				print("At bottom limit")
				return 0
			
			if not GPIO.input(8):
				self.currentCarPosition = self.currentCarPosition
				self.carStatus = 'bottom'
				print("At top limit")
				return stepsCompleted
				
			# Wait before doing the next step
			time.sleep(self.stepDelayTime)

		carStatus = 'ready'
		Return stepsCompleted

