# Hall button presses end up here
#  The HallLampInitialize sets up the callbacks
#  Turns on lamp and sets value in config.FloorStopList

import RPi.GPIO as GPIO
import config

lampPin = 0

def HallButtonCallBack(channel):
	print("HallButtonCallBack: Channel ", channel)

	# Use BCM GPIO references
	# instead of physical pin numbers 
	# GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BCM)	
	GPIO.setwarnings(False)
	
	buttonsDown = [0,3,4,5,6]
	buttonsUp   = [0,7,8,9,10]
			
	# TODO:Explain what does rising edge refer to?
	print ("HallButtonCallBack: Rising edge detected on port: ",channel)  
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
	elif   channel ==  7:
		floor=1
		lampPin = 15
	elif channel ==  8:
		floor = 2
		lampPin = 16
	elif channel ==  9:
		floor = 3
		lampPin = 17
	elif channel == 10:
		floor = 4
		lampPin = 18

	config.HallStopList[abs(floor)] = floor
	
	# Display floor number pressed
	print("HallButtonCallBack: Pressed floor: ", floor)

	
	if config.HallStopList[floor] == 0:
		GPIO.output(lampPin,False)
	else:
		GPIO.output(lampPin,True)
	
	print ("HallButtonCallBack: ", config.HallStopList)
