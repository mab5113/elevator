# Global identifiers to be imported into module

FloorStopList    = [0,0,0,0,0,0]
CarFloorStopList = [0,0,0,0,0,0]

HallStopListUp   = [0,0,0,0,0,0]
HallStopListDown = [0,0,0,0,0,0]

CarCurrentFloor  = [0,0,0,0,0,0]

CarLampsPins  = [0,19,20,21,22,23]
CarButtonPins = [0,14,15,16,17,18]

HallLampPinsDown = []
HallLampPinsUp   = []

HallButtonPinsDown = []
HallButtonPinsUp  =[]

# floor positions for the stepper motor
#  convet to lists (of lists) so each car can have its own list
FloorStepList=[0,-10000,2200,4400,5000,10000]

CarCurrentStatus = [0,0,0,0,0,0,0,0]
CarCurrentStepPosition =[0,0,0,0,0,0,0,0]
CarStepWaitTime = [0, .0015, .0015, .0015, .0015, .0015, .0015, .0015, .0015]
CarTopPosition = [0,7400,7400,7400,7400,7400,7400,7400,7400,7400,7400]

IpHall='192.168.254.69/24'

#IpHall='10.81.104.31/24'
IpCar1='10.81.104.32/24'
IpCar2='10.81.104.33/24'
IpCar3='10.81.104.34/24'
IpMatt='10.81.104.35/24'
IpCory='10.81.104.36/24'
IpKyle='10.81.104.27/24'
IpSean='10.81.104.28/24'
IpRyan='10.81.104.29/24'
IpChristian='10.81.104.30/24'

