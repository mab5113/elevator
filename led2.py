Python 2.7.9 (default, Sep 17 2016, 20:26:04) 
[GCC 4.9.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print 'LED on'
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print 'LED off'
GPIO.output(18, GPIO.LOW)
>>> 
