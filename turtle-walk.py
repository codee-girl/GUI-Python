import turtle as t
import random

timmy = t.Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270, 500]
timmy.pensize(20)
timmy.speed("fastest")

for _ in range(300):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

