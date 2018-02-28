

CarFloorsTotal = 5			# Number of floors for this elevator car 

CarCurrntFloorSteps = 0			# the number of steps from the 1st floor to the current position
CarCurrentFloor = 0			3 The current floor#
CarCurrentStatus - 'dnd'  		# floor#, 'moving', ;dnd' , 'fault'
CarCurrentDirection = 'stopped'  	# up, down, stopped

CarParkFloor = 1			# Floor to return when no activity, usually 1st floor

# delays and timing
CarTravelSpeed = .003 			# Car movement speed when moving up or down
CarDoorOpenSpeed = .003			# Car door open speed
CarDoorCloseSpeed = .003		# Car door close speed
CarDoorCloseDelay = 10			# Car door close wait Time (seconds)


CarTotalStep2Top = 0			# Car step count to move from bottom to top floor
CarNoActivityTime = 50			# time with no car requests (seconds)

CarFloorStopList = [0,0,0,0,0] 		# floor number(s) to stop. Updated from the System manager for Hallway calls
CarFloorStepList = [0,250,500,750,1000]	# the stepper motor count needed to move to a floor from the bottom floor
					#   updated when the car is initializes for recalibrated

CarFloorCount = 0			# Count of floors the car has moved

import CarStartUp.py			# run the start up initialization