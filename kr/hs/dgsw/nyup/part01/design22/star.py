import turtle as t
import math as m

t.setup(800, 800)
t.shape('turtle')
t.speed(10)
t.pencolor('black')
t.width(5)
t.up(); t.goto(0, 360); t.down()

p = m.pi
r = 360

for i in range(0, 721, 144):
    a = p * i / 180.0
    x = r * m.sin(a)
    y = r * m.cos(a)
    t.goto(x, y)

t.pencolor('white')
t.width(3)
t.up(); t.goto(0, 360); t.down()

for i in range(0, 721, 144):
    a = p * i / 180.0
    x = r * m.sin(a)
    y = r * m.cos(a)
    t.goto(x, y)

t.done()
