
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

print  'LED on'
GPIO.output(18,GPIO.LOW)

time.sleep(1)

print ('LED off')
GPIO.output(18, GPIO.HIGH)



print ( sys.version_info[0] )
  
print  (sys.version_info[1])

