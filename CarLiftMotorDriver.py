
#!/usr/bin/python

# CarLiftMotorDriver
# Low level driver for the lift stepper motor 

import sys
import time
import RPi.GPIO as GPIO
 
def CarLiftMotorDriver(direction, RequestedSteps, waitTime):
totalSteps = 0 

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [17,22,23,24]     

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

#Define GPIO for top or bottom limit switch
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN
  
# Set all pins as output
for pin in StepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
 
# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
      
StepCount = len(Seq)
StepDir = direction    # Set to 1 or 2 for clockwise
						# Set to -1 or -2 for anti-clockwise

StepCounter = RequestedSteps
 
# main loop
for StepCounter in range(steps):
   for pin in range(0, 4):
    xpin = StepPins[pin]
    if Seq[StepCounter][pin]!=0:
      # print "  enable GPIO %i" %(xpin)
      GPIO.output(xpin, True)
    else:
        GPIO.output(xpin, False)
 
  StepCounter += StepDir
  if not GPIO.input(4):
     break
 
  # If we reach the end of the sequence start again
  if (StepCounter>=StepCount):


    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount+StepDir
 
  # Wait before moving on
  time.sleep(WaitTime)
  totalSteps += 1
  
 return totalSteps 
