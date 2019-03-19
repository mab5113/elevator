import time
import RPi.GPIO as GPIO
import config

# Allow for hystersis of the limit switches
#  It will take n steps for the limit switch to actually open
# LimitSwitchHystersis = 300 <---- Not needed

#class StepperDriverClass(id, steps, StepMotorPins, limitSwitchBottomPin, limitSwitchTopPin):
class StepperDriverClass():
	def __init__(self): 
	#def __init__(self, StepMotorPins, LimitSwitchTopPin, LimitSwitchBottomPin ): 
		# Variables defined here are instance variables available in instances of the class only
		#StepMotorPins = StepMotorPins 		# [6,5,4,3]	
		#LimitSwitchBottomPin = limitSwitchBottomPin  	# = 7
		#LimitSwitchTopPin = limitSwitchTopPin  	# = 8
		print ( 'init')
		pass
	
	# Variables defined here are called class variables and are in all instances of this class
	#   Each group of 4 values (bits) are applied to the H-Bridge controller inputs 
	#     by the RPi outputs pins
	#  H-bridge sequence in manufacturers datasheet
	#  Notice that from step to step, only one bit changes

	Seq = [[1,0,0,1], [1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1]]
	#Initializes starting position and counter for steps taken
	
	currentPosition = 0
	grandTotalSteps = 0
	id = 1  # remove
	
	StepMotorPins = [6,5,4,3]
	LimitSwitchBottomPin = 7	
	LimitSwitchTopPin    = 8


	
	# Use BCM GPIO references instead of physical pin numbers
	GPIO.setmode(GPIO.BCM)
	
	#set up top and bottom floor limit switches
	GPIO.setup(LimitSwitchBottomPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(LimitSwitchTopPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

	# Define GPIO signals to use
	# Physical pins 5, 7, 29, 31
	# GPIO3, GPIO4, GPIO5, GPIO6
	
	# Set all pins as output and set to sink current
	for pin in StepMotorPins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)
		
	StepSeqCounter = 0

	def move2Position(self, Position):
					
		StepMotorPins = [6,5,4,3]
		LimitSwitchBottomPin = 7	
		LimitSwitchTopPin    = 8
		id =1

		if config.CarCurrentStepPosition[1] > Position:
			#Sets the stepper direction to down
			stepDir = -1
		else:
			#Sets the stepper direction to up
			stepDir = 1

		while config.CarCurrentStepPosition[id] != Position:
			#Each loop will rotate the stepper motor one step

			if not GPIO.input(LimitSwitchBottomPin) and stepDir == -1:
				#At bottom, input is low/false when switch closes
				# can't go lower than bottom
				print("bottom limit reached")
				config.CarCurrentStepPosition[id] = 0
				for pin in StepMotorPins:
					GPIO.output(pin, False)
				return
			
			elif not GPIO.input(LimitSwitchTopPin) and stepDir == 1:
				#At top, input is high/true when switch closes
				# can't go higher than top
				print("top limit reached")
				print (config.CarCurrentStepPosition[id])
				for pin in StepMotorPins:
					GPIO.output(pin, False)
				return

			# Set the RPi 4 output pins the the values in the current sequence item		
			for pin in range(0, 4):
				xpin = StepMotorPins[pin]
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
	
			config.CarCurrentStepPosition[1] += stepDir

			time.sleep(config.CarStepWaitTime[1]) # Wait before moving on to next step
			#time.sleep(.02) # Wait before moving on to next step
		
	