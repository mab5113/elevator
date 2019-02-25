# Global identifiers to be imported int module

FloorStopList = [0,0,1,0,0,0]
HallStopList = [0,0,0,0,0,0]

# Car1 is position 1 in the list
# Car 2 is postion 2 in the list
#  etc.
# Might encode status also
#   1= going up
#  -1 = going down
#   0 = not in operation
Can handle as many cars approprate
car1CurrentFloor =  [0,0,0,0,0,0]

# floor positions for the stepper motor
# Might convet to lists (of lists) so each car can have its own list
FloorStepList=[0,-10000,2200,4400,5000,10000]

CarCurrentFloor = 0
FloorCurrentStep = 0
CarCurrentDirection = 0
CarCurrentStatus = 'stopped'
CarCurrentStepPosition = 0
CarStepWaitTime = .002
CarTopPosition = 7400

HallipAddress = '10.81.104.120'
CaripAddress1 = '10.81.104.121'
CaripAddress2 = '10.81.104.122'

CarFloorLampsPins=[0,19,20,21,22,23]
carFloorLamp1= 19
carFloorLamp2 = 20
carFloorLamp3 = 21
carFloorLamp4 = 22
carFloorLamp5 = 23
