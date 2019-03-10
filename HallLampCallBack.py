# Hall button presses end up here
#  The HallLampInitialize sets up the callbacks
#  Turns on lamp and sets value in config.FloorStopList

import RPi.GPIO as GPIO
import config

lampPin = 0

def HallLampCallBack(channel):  

	# Use BCM GPIO references
	# instead of physical pin numbers 
	# GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BCM)	
	GPIO.setwarnings(False)
			
	# TODO:Explain what does rising edge refer to?
	print ("HallLampCallBack: Rising edge detected on port: ",channel)  
	floor = 0
	
	# DOWN BUTTONS (there is no floor 1 down button
	if   channel == 3:
		floor= -2
		lampPin = 11
	elif channel == 4:
		floor= -3
		lampPin = 12
	elif channel == 5:
		floor= -4
		lampPin = 13
	elif channel == 6:
		floor= -5
		lampPin = 14
			
	#UP BUTTONS (there is no floor 5 up button)
	if   channel ==  7:
		floor=1
		lampPin = 15
	elif channel ==  8:
		floor=2
		lampPin = 16
	elif channel ==  9:
		floor=3
		lampPin = 17
	elif channel == 10:
		floor=4
		lampPin = 18

	if floor < 0:
		config.HallStopList[floor] = -1
		floor = abs(floor)
	else:
		config.HallStopList[floor] = 1
	
	# Display floor number pressed
	print("HallLampCallBack: Pressed ", floor)

	
	if config.HallStopList[floor] != 0:
		config.HallStopList[floor]=0
		GPIO.output(lampPin,False)
	else:
		config.HallStopList[floor]=1
		GPIO.output(lampPin,True)
	
	print ("HallLampCallBack: ", config.HallStopList)
