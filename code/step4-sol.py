import turtle
import random

width = 300
height = 400
window = turtle.Screen()
window.setup(width, height)
window.tracer(0)

N = 10 # Number of balls
balls = []
velocities = []

color = ["blue",
        "yellow",
        "red",
        "darkgreen", 
        "cyan", 
        "violet",
        "magenta",
        "orange",
        "purple", 
        "navy", 
        "brown", 
        "maroon",
        "turquoise", 
        "lightgreen", 
        "green", 
        "skyblue", 
        "black", 
        "gold",
        "gray"]

for i in range(N):
    balls.append(turtle.Turtle())
    balls[i].penup()
    balls[i].shape("circle")
    balls[i].color(color[i%len(color)])

    # Set random starting position
    balls[i].setx(random.randint(0,height / 4))
    balls[i].sety(random.randint(0,height / 4))

    # Set random starting velocities
    velocities.append([random.randint(-width/10,width/10),0])


gravity = -9.81
Delta_t = 0.008
i = 0
while True:
    for i in range(N):
        velocities[i][1] = gravity*Delta_t + velocities[i][1]
        balls[i].setx(velocities[i][0]*Delta_t + balls[i].xcor())
        balls[i].sety(velocities[i][1]*Delta_t + balls[i].ycor())

        if balls[i].ycor() < -height / 2 or balls[i].ycor() > height / 2:
            velocities[i][1] = -velocities[i][1]
        if balls[i].xcor() < -width / 2 or balls[i].xcor() > width / 2:
            velocities[i][0] = -velocities[i][0]

        # Check for collisions
        for j in range(N):
            if abs(balls[i].xcor() - balls[j].xcor()) < 10 \
                    and abs(balls[i].ycor() - balls[j].ycor()) < 10:
                        vh = velocities[i]
                        velocities[i] = velocities[j]
                        velocities[j] = vh

    #update window
    i=(i+1)%10
    if not i:
        window.update()
