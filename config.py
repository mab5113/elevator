# Global identifiers to be imported int module

FloorStopList   = [0,0,0,0,0,0]
HallStopList    = [0,0,0,0,0,0]
carCurrentFloor =  [0,0,0,0,0,0]


# floor positions for the stepper motor
#  convet to lists (of lists) so each car can have its own list
FloorStepList=[0,-10000,2200,4400,5000,10000]

CarCurrentStatus = 'stopped'
CarCurrentStepPosition = 0
CarStepWaitTime = .0015
CarTopPosition = 7400

CarFloorLampsPins=[0,19,20,21,22,23]
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

