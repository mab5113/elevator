import time
import RPi.GPIO as GPIO
from CarLampCallBack import CarLampCallBack

def CarLampMonitor(operation,floor, value):
	if operation =='clearall':
		pass
	elif operation=='floor':
		pass
	elif operation=='initialize':

		# Use BCM GPIO references
		# instead of physical pin numbers
		#GPIO.setmode(GPIO.BOARD)
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
			
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

		time.sleep(1)
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
	
		GPIO.add_event_detect(14, GPIO.RISING, callback=CarLampCallBack, bouncetime=400)  
		GPIO.add_event_detect(15, GPIO.RISING, callback=CarLampCallBack, bouncetime=400)  
		GPIO.add_event_detect(16, GPIO.RISING, callback=CarLampCallBack, bouncetime=400)  
		GPIO.add_event_detect(17, GPIO.RISING, callback=CarLampCallBack, bouncetime=400)  
		GPIO.add_event_detect(18, GPIO.RISING, callback=CarLampCallBack, bouncetime=400)  