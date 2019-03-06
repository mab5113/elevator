<h1 style="color:blue;">
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

<h1> MASTER (raspberry pi) </h1>

<p>
gets button presses<br>
Gets car location<br>
Maintain floor lists<br>
Send floor stop lists to cars<br>
Computes car movement priority <br>
</p>


<h1>CAR 1 control (raspberry pi) </h1>
<p>
Move car up/down<br>
Controls door<br>
Knows location<br>
Monitor floor button<br>
Turns lamp on/off<br>
Send car info to master<br>
Receives floor stop list from master<br>
</p>

<h1>CAR 2 control (Raspberry PI) </h1>
<p>
Move car up/down<br>
Controls door<br>
Knows location<br>
Monitor floor button<br>
Turns lamp on/off<br>
Send car info to master<br>
Receives floor stop list from master<br>
</p>

<h1>Monitor Hallway Buttons (Raspberry PI)</h1>
<p>
Controls Hall Way LAMP<br>
Send button info to master<br>
</p>