import turtle as t
from math import sin, cos, pi

t.setup(800, 800)
t.shape('turtle')
t.speed(10)
t.pencolor('red')
t.width(5)
t.up(); t.goto(-360, 0); t.down()

p = pi

for i in range(0, 361):
    a = p * i / 180.0
    x = i * 2 - 360
    y = 300 * sin(a)
    print("Printing SIN graph...")
    t.goto(x, y)
print('Complete printing SIN graph.')

t.pencolor('blue')
t.up(); t.goto(-360, 300); t.down()

for i in range(0, 361):
    a = p * i / 180.0
    x = i * 2 - 360
    y = 300 * cos(a)
    print("Printing COS graph...")
    t.goto(x, y)
print('Complete printing COS graph.')

t.done()
