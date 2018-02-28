

Def DoorOpenClose(openClose, steps, openSpeed, closeSpeed):
If Operation = 'open':
For i in range(0,steplimit)
	If limitswitch closes;
		Return ‘ok’
##Step the motor in open direction
# Return ‘99 door open failure’

elIf  Operation = close:

For i in range(0,steplimit)
	If limitswitch closes;
		Return ‘0 Door is closed’
	If Breakbeam = true
		Return ‘1 Break Beam Tripped’
	If doorForceSwitch closed
		Return ‘2 Door Blocked’
	If cancelbuttonPressed
			Return ‘3 Door Open Button Pressed’

#Continue to Step the motor in open direction
Return ‘99 door open failure’
Else
	Return ‘99 invalid door command’
