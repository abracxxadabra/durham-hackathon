import turtle

ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")

# Now we introduce gravity instead of prescribing the motion
# Recall F=ma
# here a is acceleration, m is the mass of the ball (1 for now)
# and F is the force acting on the ball (currently only gravity)
# This means
#   v(t+Delta_t) = g*Delta_t+v(t)
#   x(t+Delta_t) = v(t)*Delta_t+x(t)
gravity = -9.81
Delta_t = 0.05
v = [0, 0]

while True:
    # TODO: update velocity and position
