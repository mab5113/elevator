import time
import RPi.GPIO as GPIO
import config

def CarLampCallBack(channel):  

	# Use BCM GPIO references
	# instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
			
	floor = 0
	print ("Rising edge detected on port: ",channel)  
	if channel == 14: floor=1			
	elif channel == 15: floor=2
	elif channel == 16: floor=3
	elif channel == 17: floor=4
	elif channel == 18: floor=5
	
	print('CarLampCallBack: Floor', floor)
	
	pin=config.CarLampsPins[floor]
	if config.FloorStopList[floor] == 0:
		config.FloorStopList[floor]=1
		GPIO.output(pin,False)
	else:
		config.FloorStopList[floor]=0
		GPIO.output(pin,True)
	
	print ('CarLampCallBack: StopList: ', config.FloorStopList)
