.This project developes the code for a model elevator of 2 cars runs on a raspberry pi 3

to clone 
-git clone https://github.com/sdev265/elevator.git

HISTORY
One year ago AHI funded the building of a tabletop model prototype. 
The general requirements was the prototype controller and software must control a five (5) floor elevator prototype. 
There was an understanding that project was likely to be more complex than initially anticipated.

The prototype was constructed to discover and identify issues. 
The previous team confirmed that Raspberry Pi(s) are capable of controlling a prototype model elevator

Current Status
With the success of the prototype, AHI has agreed to continue funding the project to scale up the model and add features with a new team of developers. 
The model and software will implement as many “normal” passenger elevator functions as possible. 

<h1 style= "color:green;"> MASTER (raspberry pi)

<p>
#gets button presses<br>
#Gets car location<br>
#Maintain floor lists<br>
#Send floor stop lists to cars<br>
#Computes car movement priority <br>
</p>


CAR 1 control (raspberry pi)

#Move car up/down
#Controls door
#Knows location
#Monitor floor button
#Turns lamp on/off
#Send car info to master
#Receives floor stop list from master

CAR 2 control (Raspberry PI)

#Move car up/down
#Controls door
#Knows location
#Monitor floor button
#Turns lamp on/off
#Send car info to master
#Receives floor stop list from master


Monitor Hallway Buttons (Raspberry PI)

#Controls Hall Way LAMP
#Send button info to master