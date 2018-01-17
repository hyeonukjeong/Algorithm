import turtle as t
import math as m

t.setup(800, 800)
t.shape('turtle')
t.speed(10)
t.pencolor('black')
t.width(5)
t.up(); t.goto(360, 0); t.down()

p = m.pi
a = 360
b = 280

for i in range(0, 361):
    r = p * i / 180.0
    x = a * m.cos(r)
    y = b * m.sin(r)
    t.goto(x, y)

t.done()
