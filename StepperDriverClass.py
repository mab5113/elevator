import time
import RPi.GPIO as GPIO
import config

class StepperDriverClass():
	stepDelayTime = .004
	currentPosition = 0
	grandTotalSteps = 0
	def __init__(self): 
		pass
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
	
	StepPins = [3,4,5,6]
							   
	# Set all pins as output
	for pin in StepPins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)
		
	#5,6,2,3,4,5	
	StepCounter = 0

	def DoSteps(self, moveSteps):
		print('stepdriver',moveSteps)
		Seq = [[1,0,0,1], [1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1]]
		StepCount = len(Seq)


		totalSteps = 0

		# Allow for hystersis of the limit switches
		#  It will take n steps for the limit switch to open
		LimitSwitchHystersis = 300

		if moveSteps < 0:
			stepDir = 1
			moveSteps = abs(moveSteps)
			if not GPIO.input(7):
				print("bottom limit")
				#return 0
		else:
			stepDir = -1
			if not GPIO.input(8) :
				print("top limit")
				#return 999999
			
		if not GPIO.input(7) and stepDir ==1:
			print("bottom limit")
			return

		if not GPIO.input(8) and stepDir ==1:
			print("Top limit")
			return
				
	
		while totalSteps < moveSteps:
			#print StepCounter,
			#print Seq[StepCounter]
			
			for pin in range(0, 4):
				xpin = self.StepPins[pin]
				if Seq[self.StepCounter][pin]!=0:
					#      print "  enable GPIO %i" %(xpin)
					GPIO.output(xpin, True)
				else:
					#      print " Disable GPIO %i" %(xpin)
					GPIO.output(xpin, False)
			
			self.StepCounter += stepDir
			
			# If we reach the end of the sequence start again
			if (self.StepCounter>=StepCount):
				self.StepCounter = 0
			
			if (self.StepCounter<0):
				self.StepCounter = StepCount+stepDir
			
			# Wait before moving on
			time.sleep(config.CarStepWaitTime)
			
			totalSteps += 1
			print(totalSteps)
			
			if not GPIO.input(7) and totalSteps > 300:
				print("bottom limit")
				return
				
			
			if not GPIO.input(8) and totalSteps > 300:
				print("top limit")
				return
    				