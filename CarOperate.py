

CarCurrentFloor = 0
CarCurrentStatus - 'dnd'  		# floor#, moving, dnd , fault
CarCurrentDirection = 'stopped'  	# up, down, stopped
CarParkFloor = 1			# usually 1st floor
CarTravelSpeed = .003 			# Car movement speed when moving up or down
CarDoorOpenSpeed = .003			# Car door open speed
CarDoorCloseSpeed = .003		# Car door close speed
CarDoorCloseDelay = 10			# Car door close wait Time (seconds)
CarTotalSteps = 0			# Car step count to move from bottom to top floor
CarNoActivityTime = 50			# time with no car requests
CarDispatchList = [0,0,0,0,0] 		# floor number(s) to stop.Also updated from the System manager for Hallway calls
CarFloorStepList = [0,250,500,750,1000]	# the stepper motor count needed to move to a floor from the bottom floor
CarFloorCount = 0			# Count of floors the car has moved
CarFloorsTotal = 5			# Number of floors for this elevator car 

import CarStartUp.py			# run the start up initialization