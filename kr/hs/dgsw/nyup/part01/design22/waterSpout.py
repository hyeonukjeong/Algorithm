import turtle as t
import math as m

t.setup(800, 800)
t.speed(10)
t.pencolor('blue')
t.width(1)
t.ht()

a = m.radians(30)
b = m.radians(-30)
sx = m.sin(a)
cx = m.cos(a)
sy = m.sin(b)
cy = m.cos(b)

for z in range(-200, 200, 5):
    f = 0
    for x in range(-200, 200, 5):
        a = 500 / m.sqrt(m.sqrt((x + 50) ** 2 + (z - 50) ** 2 + 100))
        b = 500 / m.sqrt(m.sqrt((x - 50) ** 2 + (z + 50) ** 2 + 100))
        y = -2 * a - b
        px = x * cy + z * sy
        py = y * cx - (-x * sy + z * cy) * sx
        if f == 0:
            t.up(); t.goto(px, py); t.down()
            f = 1
        else:
            t.goto(px, py)

t.pencolor('black')

a = m.radians(30)
b = m.radians(-30)
sx = m.sin(a)
cx = m.cos(a)
sy = m.sin(b)
cy = m.cos(b)

for z in range(-200, 200, 5):
    f = 0
    for x in range(-200, 200, 5):
        a = 1000 / m.sqrt(m.sqrt((x - 50) ** 2 + (z + 50) ** 2 + 100))
        b = 1000 / m.sqrt(m.sqrt((x + 50) ** 2 + (z - 50) ** 2 + 100))
        y = a - b
        px = x * cy + z * sy
        py = y * cx -(-x * sy + z * cy) * sx
        if f == 0:
            t.up(); t.goto(px, py); t.down()
            f = 1
        else:
            t.goto(px, py)

t.pencolor('red')

a = m.radians(30)
b = m.radians(-30)
sx = m.sin(a)
cx = m.cos(a)
sy = m.sin(b)
cy = m.cos(b)

for z in range(-200, 200, 5):
    f = 0
    for x in range(-200, 200, 5):
        a = 500 / m.sqrt(m.sqrt((x - 50) ** 2 + (z + 50) ** 2 + 100))
        b = 500 / m.sqrt(m.sqrt((x + 50) ** 2 + (z - 50) ** 2 + 100))
        y = 2 * a + b
        px = x * cy + z * sy
        py = y * cx -(-x * sy + z * cy) * sx
        if f == 0:
            t.up(); t.goto(px, py); t.down()
            f = 1
        else:
            t.goto(px, py)

t.done()
