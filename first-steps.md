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
// output functions are configurable.  This one just appends some text
// to a pre element.
function outf(text) { 
    var mypre = document.getElementById("output"); 
    mypre.innerHTML = mypre.innerHTML + text; 
} 
function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

// Here's everything you need to run a python program in skulpt
// grab the code from your textarea
// get a reference to your pre element for output
// configure the output function
// call Sk.importMainWithBody()
function runit() { 
   var prog = document.getElementById("yourcode").value; 
   var mypre = document.getElementById("output"); 
   mypre.innerHTML = ''; 
   Sk.pre = "output";
   Sk.configure({output:outf, read:builtinRead}); 
   (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
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

<h3>Try This</h3> 
<form> 
<textarea id="firststeps" cols="40" rows="12">import turtle

ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")

while True:
    ball.sety(ball.ycor() - 1)
</textarea><br /> 
<button type="button" onclick="runit()">Run</button> 
</form> 
<div id="first-canvas"></div> 

</body> 

</html> 
If you want you can have a look a the solution [here](TODOlink).

This "simulation" is not very physical so let's try to figure out how the ball should actually move.

[Next step](/newton.html)

