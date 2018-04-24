#!/usr/bin/python
 
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
from CarDriver import CarDriver
from MotorDriver import MotorDriver

FloorStopList=[0,0,0,0,0,0]

FloorStepList=[0,0,1500,2500,3500,4500]

CarLampsPins=[0,19,20,21,22,23]

CarCurrentFloor=0

FloorCurrentStep=0

stepPos = 0
 
# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BOARD)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#def CarLampDriver():
#Test lamps
GPIO.setup(19,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

GPIO.output(19,False)
GPIO.output(20,False)
GPIO.output(21,False)
GPIO.output(22,False)
GPIO.output(23,False)

GPIO.output(19,True)
GPIO.output(20,True)
GPIO.output(21,True)
GPIO.output(22,True)
GPIO.output(23,True)

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

def my_callback(channel):  
	floor = 0
	print ("Rising edge detected on port: ",channel)  
	if channel == 14:
		floor=1
					
	elif channel == 15:
		floor=2
			
	elif channel == 16:
		floor=3
				
	elif channel == 17:
		floor=4
		
	elif channel == 18:
		floor=5
		GPIO.output(23,False)
	
	print(floor)
	
	pin=CarLampsPins[floor]
	if FloorStopList[floor] == 0:
		FloorStopList[floor]=1
		GPIO.output(pin,False)
	else:
		FloorStopList[floor]=0
		GPIO.output(pin,True)
	
	print (FloorStopList)

GPIO.add_event_detect(14, GPIO.RISING, callback=my_callback, bouncetime=400)  
GPIO.add_event_detect(15, GPIO.RISING, callback=my_callback, bouncetime=400)  
GPIO.add_event_detect(16, GPIO.RISING, callback=my_callback, bouncetime=400)  
GPIO.add_event_detect(17, GPIO.RISING, callback=my_callback, bouncetime=400)  
GPIO.add_event_detect(18, GPIO.RISING, callback=my_callback, bouncetime=400)  

print(FloorStopList)

time.sleep(0)
print(FloorStopList)

#GPIO.cleanup()
#exit()

print ('Return value:', CarDriver(-900, .006))
#CarLampDriver()
#while True:
#	elevatorDriver()