import time
import RPi.GPIO as GPIO
import config

# Allow for hystersis of the limit switches
#  It will take n steps for the limit switch to actually open
# LimitSwitchHystersis = 300 <---- Not needed

#class StepperDriverClass(id, steps, StepMotorPins, limitSwitchBottomPin, limitSwitchTopPin):
class StepperDriverClass():
	#StepMotorPins = [6,5,4,3]
	#  H-bridge sequence in manufacturers datasheet
	#  Notice that from step to step, only one bit changes
	Seq = [[1,0,0,1], [1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1]]
	
	# Use BCM GPIO references instead of physical pin numbers
	GPIO.setmode(GPIO.BCM)


	def __init__(self, id, StepMotorPins, LSTopPin, LSBottomPin ): 
		# Variables defined here are instance variables available in instances of the class only
		self.id = id
		self.StepMotorPins = StepMotorPins 	# [6,5,4,3]	
		self.LSBottomPin = LSBottomPin  	# = 7
		self.LSTopPin = LSTopPin  		# = 8
		currentPosition = 0
		grandTotalSteps = 0
		#set up top and bottom floor limit switches
		GPIO.setup(self.LSBottomPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.LSTopPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
		# Set all pins as output and set to sink current
		for pin in self.StepMotorPins:
			GPIO.setup(pin,GPIO.OUT)
			GPIO.output(pin, False)

		#pass
	
	# Variables defined here are called class variables and are in all instances of this class
	#   Each group of 4 values (bits) are applied to the H-Bridge controller inputs 
	#     by the RPi outputs pins

	def move2Position(self, Position):
		StepSeqCounter = 0	
		stepDir = 0
		
		if config.CarCurrentStepPosition[id] > Position:
			#Sets the stepper direction to down
			stepDir = -1
		else:
			#Sets the stepper direction to up
			stepDir = 1
							   
		while config.CarCurrentStepPosition[self.id] != Position:
			#Each loop will rotate the stepper motor one step

			if not GPIO.input(self.LSBottomPin) and stepDir == -1:
				#At bottom, input is low/false when switch closes
				# can't go lower than bottom
				print("bottom limit reached")
				config.CarCurrentStepPosition[id] = 0
				# Set both H-Bridges to 0 volts to not draw power
				for pin in StepMotorPins:
					GPIO.output(pin, False)
				return
			
			elif not GPIO.input(self.LSTopPin) and stepDir == 1:
				# At top, input is high/true when switch closes
				# can't go higher than top
				print("top limit reached")
				print (config.CarCurrentStepPosition[self.id])
				
				# Set both H-Bridges to 0 volts to not draw power
				for pin in self.StepMotorPins:
					GPIO.output(pin, False)
				return

			# Set the RPi 4 output pins the the values in the current sequence item		
			for pin in range(0, 4):
				xpin = self.StepMotorPins[pin]
				if self.Seq[StepSeqCounter][pin] != 0:
					GPIO.output(xpin, True)
				else:
					GPIO.output(xpin, False)
			
			StepSeqCounter += stepDir
			
			# When we reach the end of the sequence start again
			if StepSeqCounter >= len(self.Seq):
				self.StepSeqCounter = 0			
			elif StepSeqCounter < 0:
				StepSeqCounter = len(self.Seq) + stepDir
	
			config.CarCurrentStepPosition[self.id] += stepDir

			time.sleep(config.CarStepWaitTime[self.id]) # Wait before moving on to next step
		
