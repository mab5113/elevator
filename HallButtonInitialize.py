# TODO
#   Describe this Module
#   Use pin names in config - no magic pin numbers

#import time
import RPi.GPIO as GPIO

def HallButtonInitialize():

	print ('HallButton Initialize: Started')
	# Use BCM GPIO references instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	#configure the RPi inputs to pull voltage up
	# A switch closure will pull the input voltage to ground (falling edge)
	#  When the switch is opened the output voltage will go up (rising edge)
	
	# Up Hall buttons
	GPIO.setup(3, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(4, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(5, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(6, GPIO.IN,  pull_up_down=GPIO.PUD_UP) 
	
	#Down
	GPIO.setup(7, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(8, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(9, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

	#UP
	GPIO.add_event_detect(3,  GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(4,  GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(5,  GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(6,  GPIO.RISING, callback=HallButtonCallBack, bouncetime=400) 
	
	#Down
	GPIO.add_event_detect(7,  GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(8,  GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(9,  GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(10, GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	
	print ('HallButton Initialize: Completed')

	
