import time
import RPi.GPIO as GPIO
import config

class StepperDriverClass():
	currentPosition = 0
	grandTotalSteps = 0
	def __init__(self): 
		pass
	# instance variables unique to each instance
	
	# Define H-bridge sequence in manufacturers datasheet
	#  Notice that from step to step, only one bit changes
	Seq = [[1,0,0,1], [1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1]]
	
	# Use BCM GPIO references
	# instead of physical pin numbers
	GPIO.setmode(GPIO.BCM)
	
	#set up top and bottom floor limit switches
	GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(8,GPIO.IN, pull_up_down=GPIO.PUD_UP)

	# Define GPIO signals to use
	# Physical pins 5, 7, 29, 31
	# GPIO3, GPIO4, GPIO5, GPIO6
	
	StepPins = [3,4,5,6]	
	# Set all pins as output
	for pin in StepPins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)
		
	StepCounter = 0

	def move2Position(self, Position):

		if config.CarCurrentStepPosition > Position:
			StepDir = 1
		else:
			StepDir= -1

		print('stepdriver',Position)
		StepCount = len(self.Seq)
		StepPins = [3,4,5,6]
							   
		totalSteps = 0

		# Allow for hystersis of the limit switches
		#  It will take n steps for the limit switch to open
		LimitSwitchHystersis = 300

		if Position < 0:
			stepDir = 1
			Position = abs(Position)
			if not GPIO.input(7):
				print("bottom limit")
				config.CarCurrentStepPosition = 0
				return
		else:
			stepDir = -1
			if not GPIO.input(8) :
				print("top limit")
				config.CarCurrentStepPosition = 7300
				return
			
		if not GPIO.input(7) and stepDir ==1:
			print("at bottom limit")
			config.CarCurrentStepPosition=0

		if not GPIO.input(8) and stepDir ==1:
			print("at Top limit")
			config.CarCurrentStepPosition=7300
	
		while config.CarCurrentStepPosition <> Position:
			for pin in range(0, 4):
				xpin = StepPins[pin]
				if self.Seq[self.StepCounter][pin]!=0:
					GPIO.output(xpin, True)
				else:
					GPIO.output(xpin, False)
			
			self.StepCounter += StepDir
			
			# If we reach the end of the sequence start again
			if (self.StepCounter>=StepCount):
				self.StepCounter = 0
			
			if (self.StepCounter<0):
				self.StepCounter = StepCount+StepDir
			
			# Wait before moving on
			time.sleep(config.CarStepWaitTime)
	
			totalSteps += 1
			config.CarCurrentStepPosition += -stepDir

			if not GPIO.input(7) and stepDir ==1:
				print("bottom limit")
				config.CarCurrentStepPosition=0
				return
			
			if not GPIO.input(8) and stepDir ==-1:
				print("top limit")
				config.CarCurrentStepPosition = 7300
				return
