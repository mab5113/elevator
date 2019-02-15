#!/usr/bin/python3
 
# Import required libraries

import config
import time


from HallLampMonitor import HallLampMonitor
	
def HallMain(id,ipaddress):
	HallLampMonitor('initialize',0,0)

	time.sleep(30)