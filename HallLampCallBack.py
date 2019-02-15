import time
import RPi.GPIO as GPIO
import config

def HallLampCallBack(channel):  


	# Use BCM GPIO references
	# instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
			
	floor = 0
	print ("Rising edge detected on port: ",channel)  
	
	# DOWN BUTTONS

					
	if channel == 3:
		floor=2
			
	elif channel == 4:
		floor=3
				
	elif channel == 5:
		floor=4
		
	elif channel == 6:
		floor=5
	if channel == 2:
		floor=1
			
	#UP BUTTONS		
	if channel == 7:
		floor=1
	elif channel == 8:
		floor=2
			
	elif channel == 9:
		floor=3
				
	elif channel == 10:
		floor=4
		
	elif channel == 11:
		floor=5
	
	print(floor)
	
	pin=config.CarLampsPins[floor]
	if config.FloorStopList[floor] == 0:
		config.FloorStopList[floor]=1
		GPIO.output(pin,False)
	else:
		config.FloorStopList[floor]=0
		GPIO.output(pin,True)
	
	print (config.FloorStopList)