---
layout: default
---

##  What happens when we drop an elastic ball?

We've got a ball (of mass m).
We'll try to simulate it using the python library turtle.

The code below will give you a "ball" object.
In the loop try to modify the position of the ball so it begins to fall.

You will need only two python functions:
1. `ball.sety(val)` sets the position of ball to `val`
1. `ball.ycor()` gets the current position of ball

Both of these functions are for the y-coordinate of the ball.
The same functions exist for the x-coordinate, but we don't need those so far.

<html> 
<head> 
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js" type="text/javascript"></script> 
<script src="js/skulpt.min.js" type="text/javascript"></script> 
<script src="js/skulpt-stdlib.js" type="text/javascript"></script> 

</head> 

<body> 

<script type="text/javascript"> 

function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}



function runit() {
   var prog = document.getElementById("firststeps").value; 
   Sk.configure({read:builtinRead}); 
   (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'first-canvas';
   var myPromise = Sk.misceval.asyncToPromise(function() {
       return Sk.importMainWithBody("<stdin>", false, prog, true);
   });
   myPromise.then(function(mod) {
       console.log('success');
   },
       function(err) {
       console.log(err.toString());
   });
}
</script> 

<h3>First Steps:</h3> 
<form> 
<textarea id="firststeps" cols="60" rows="12">import turtle

ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")

while True:
    #TODO: Place your code here
</textarea><br /> 
<button type="button" onclick="runit()">Run</button> 
</form>

<div id="first-canvas"></div> 

</body> 

</html> 
If you want you can have a look a the solution [here](/code/step-1-sol.py).

This "simulation" is not very physical so let's try to figure out how the ball should actually move.

[Next step](/durham-hackathon/newton.html)

