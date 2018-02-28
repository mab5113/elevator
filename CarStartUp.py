
def CarStartUp():

# called when car computer is turned on
Set status to dnd
Move to first floor
Move to top Floor and set step count
Initialize CarFloorStepList  ( example: if step count = 1000)
Divide steps by floorCount -1
Floor 1 = 0
Floor 2 = 250 (1000/4)
Floor 3 = 500 (1000/4*2)
Floor 4 = 750 (1000/4*3)
Floor 5 = 1000 (1000/4*4)
Move to first floor 
set current car floor to 1 
Set current car direction to up
Turn on car direction up light
Flash car floor Indicators and set to off
Clear CarDispatchList to all zeros
Set global variables to default values
Send Ready to System Manager

Note: System Manage may respond with new global variable values
