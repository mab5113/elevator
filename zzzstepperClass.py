<<<<<<< HEAD

  
=======
>>>>>>> b61d8f17793127ab473e7f4927de35bdd3fb4bc2
#!/usr/bin/python
 
# Import required libraries
import sys
import             time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO signals to use
<<<<<<< HEAD
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [17,22,23,24]
=======
# Physical pins 5,7,29,31
# GPIO3,GPIO4,GPIO5,GPIO6
StepPins = [3,4,5,6]
>>>>>>> b61d8f17793127ab473e7f4927de35bdd3fb4bc2
                                   
# Set all pins as output
for pin in StepPins:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
 
<<<<<<< HEAD
# Define advanced sequence
# as shown in manufacturers datasheet
=======
#set up top and bottom floor limit switches
print ('set limit switch IO')
GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8,GPIO.IN, pull_up_down=GPIO.PUD_UP)

totalSteps = 0

# Define  sequence in manufacturers datasheet
>>>>>>> b61d8f17793127ab473e7f4927de35bdd3fb4bc2
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]

Seq3 = [[1,1,0,0],
       [0,1,1,0],
       [0,0,1,1],
       [1,0,0,1]]
<<<<<<< HEAD

       
StepCount = len(Seq)
StepDir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise
 
# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)

WaitTime = .005
 
# Initialise variables
StepCounter = 0
 
# Start main loop
while True:
 
  print StepCounter,
  print Seq[StepCounter]
 
  for pin in range(0, 4):
    xpin = StepPins[pin]
    if Seq[StepCounter][pin]!=0:
      print "  enable GPIO %i" %(xpin)
      GPIO.output(xpin, True)
    else:
      print " Disable GPIO %i" %(xpin)
      GPIO.output(xpin, False)
 
  StepCounter += StepDir
 
  # If we reach the end of the sequence
  # start again
  if (StepCounter>=StepCount):


    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount+StepDir
 
  # Wait before moving on
  time.sleep(WaitTime)
=======

       
StepCount = len(Seq)
StepDir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise

if not GPIO.input(7):
   print("top Limit closed")
   StepDir = -1

if not GPIO.input(8):
   print("bottom limit closed")
   StepDir = 1

#exit() 


WaitTime = .001
 
# Initialise variables
StepCounter = 0
 
# Start main loop
while True:
 
  print StepCounter,
  print Seq[StepCounter]
 
  for pin in range(0, 4):
    xpin = StepPins[pin]
    if Seq[StepCounter][pin]!=0:
#      print "  enable GPIO %i" %(xpin)
      GPIO.output(xpin, True)
    else:
#      print " Disable GPIO %i" %(xpin)
      GPIO.output(xpin, False)
 
  StepCounter += StepDir
 
  # If we reach the end of the sequence
  # start again
  if (StepCounter>=StepCount):
    StepCounter = 0

  if (StepCounter<0):
    StepCounter = StepCount+StepDir
 
  # Wait before moving on
  time.sleep(WaitTime)

  totalSteps += 1
  print(totalSteps)

  if not GPIO.input(7) and totalSteps > 300:
    print("bottom limit")
    exit()
>>>>>>> b61d8f17793127ab473e7f4927de35bdd3fb4bc2

  if not GPIO.input(8) and totalSteps > 300:
    print("top limit")
    exit()
