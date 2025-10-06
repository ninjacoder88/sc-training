import turtle as t
import time
import random

def playGame():
    t.begin_fill("orange")
    t.goto(100, 100)
    t.circle(50)
    t.end_fill()
    t.write("Are you ready?", True, ("Arial", 24, "normal"))

    t.begin_fill("orange")
    t.goto(500, 500)
    t.circle(50)
    t.end_fill()
    t.write("Are you ready?", True, ("Arial", 24, "normal"))

t.screensize(750, 750)
t.setup(1000, 1000, None, None)
t.speed(10)

t.write("Click to Start", True, "center", ("Arial", 24, "normal"))
onclick(playGame)

t.mainloop()