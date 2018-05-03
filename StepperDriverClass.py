import time
import RPi.GPIO as GPIO
import config


# Allow for hystersis of the limit switches
#  It will take n steps for the limit switch to open
# LimitSwitchHystersis = 300


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
	# Set all pins as output and set to sink current
	for pin in StepPins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)
		
	StepSeqCounter = 0

	def move2Position(self, Position):
		totalSteps = 0

		if config.CarCurrentStepPosition > Position:
			StepDir = 1
		else:
			StepDir= -1

		#print('stepdriver', Position)
		
		StepPins = [3,4,5,6]
							   

		if Position < 0:
			stepDir = 1			
		else:
			stepDir = -1


		print (Position)
				
		while config.CarCurrentStepPosition <> Position:

			if not GPIO.input(7) and stepDir == 1:
				#input goes low/false when switch closes
				# can't go lower than bottom
				print("at bottom limit")
				config.CarCurrentStepPosition = 0
				return
			elif not GPIO.input(8) and stepDir ==-1:
				print("top limit")
				config.CarCurrentStepPosition = 7300
				return

			for pin in range(0, 4):
				print(pin)
				xpin = StepPins[pin]
				if self.Seq[self.StepSeqCounter][pin]!=0:
					GPIO.output(xpin, True)
				else:
					GPIO.output(xpin, False)
			
			self.StepSeqCounter += StepDir
			
			# If we reach the end of the sequence start again
			if (self.StepSeqCounter>=len(self.Seq)):
				self.StepCounter = 0			
			elif (self.StepSeqCounter<0):
				self.StepSeqCounter = len(self.Seq) + StepDir
	
			totalSteps += 1
			config.CarCurrentStepPosition += -stepDir

			
			time.sleep(config.CarStepWaitTime) # Wait before moving on
