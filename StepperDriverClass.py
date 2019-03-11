import time
import RPi.GPIO as GPIO
import config

# Allow for hystersis of the limit switches
#  It will take n steps for the limit switch to actually open
# LimitSwitchHystersis = 300 <---- Not needed

#class StepperDriverClass(steps, stepPins, limitPins):
class StepperDriverClass():
	#Initializes starting position and counter for steps taken
	currentPosition = 0
	grandTotalSteps = 0
	def __init__(self): 
		pass

	# instance variables unique to each instance
	
	# Define H-bridge sequence in manufacturers datasheet
	#  Notice that from step to step, only one bit changes

	Seq = [[1,0,0,1], [1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1]]
	
	# Use BCM GPIO references instead of physical pin numbers
	GPIO.setmode(GPIO.BCM)
	
	#set up top and bottom floor limit switches
	GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(8,GPIO.IN, pull_up_down=GPIO.PUD_UP)

	# Define GPIO signals to use
	# Physical pins 5, 7, 29, 31
	# GPIO3, GPIO4, GPIO5, GPIO6
	

	StepPins = [6,5,4,3]	
	# Set all pins as output and set to sink current
	for pin in StepPins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)
		
	StepSeqCounter = 0

	def move2Position(self, Position):
		totalSteps = 0

		if config.CarCurrentStepPosition > Position:
			#Sets the stepper direction to down
			stepDir = -1
		else:
			#Sets the stepper direction to up
			stepDir = 1

		StepPins = [6,5,4,3]
							   
		while config.CarCurrentStepPosition != Position:
			#Each loop will rotate the stepper motor one step

			if not GPIO.input(7) and stepDir == -1:
				#At bottom, input is low/false when switch closes
				# can't go lower than bottom
				print("bottom limit reached")
				config.CarCurrentStepPosition = 0
				for pin in StepPins:
					GPIO.output(pin, False)
				return
			elif not GPIO.input(8) and stepDir == 1:
				#At top, input is high/true when switch closes
				# can't go higher than top
				print("top limit reached")
				print (config.CarCurrentStepPosition)
				for pin in StepPins:
					GPIO.output(pin, False)

				return

			#TODO: Figure out this code block
			for pin in range(0, 4):
				xpin = StepPins[pin]
				if self.Seq[self.StepSeqCounter][pin] != 0:
					GPIO.output(xpin, True)
				else:
					GPIO.output(xpin, False)
			
			self.StepSeqCounter += stepDir
			
			# When/If we reach the end of the sequence start again
			if self.StepSeqCounter >= len(self.Seq):
				self.StepSeqCounter = 0			
			elif self.StepSeqCounter<0:
				self.StepSeqCounter = len(self.Seq) + stepDir
	
			totalSteps += 1
			config.CarCurrentStepPosition += stepDir

			
			time.sleep(config.CarStepWaitTime) # Wait before moving on to next step
		
		#make sure motor is not drawing current
		for pin in StepPins:
			GPIO.output(pin, False)

