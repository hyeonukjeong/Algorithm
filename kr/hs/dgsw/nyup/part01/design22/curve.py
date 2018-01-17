import turtle as t
from math import sin, cos, radians

t.setup(800, 800)
t.shape('turtle')
t.speed(10)
t.pencolor('black')
t.up(); t.goto(-360, 0); t.down()

for i in range(-360, 360):
    a = radians(i)
    s = 150 * sin(a * 5) * sin(a * 2)
    c = 100 * cos(a) * cos(a * s)
    t.goto(i, s)
    t.goto(i, c)

t.done()
