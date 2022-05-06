import turtle

ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")

# Now we set the screen height and width
width = 600
height = 800
window = turtle.Screen()
window.setup(width, height)

gravity = -9.81
Delta_t = 0.05
v = [25, 0]

while True:
    v[1] = gravity*Delta_t + v[1]
    ball.setx(v[0]*Delta_t + ball.xcor())
    ball.sety(v[1]*Delta_t + ball.ycor())

    if ball.ycor() < -height / 2 or ball.ycor() > height / 2:
        v[1] = -v[1]
    if ball.xcor() < -width / 2 or ball.xcor() > width / 2:
        v[0] = -v[0]
