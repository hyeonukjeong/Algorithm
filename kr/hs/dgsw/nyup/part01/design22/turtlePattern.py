import math as m
import turtle as t

def tree(n, d, x0, y0, r):
    if n == 0:
        t.pencolor('red')
        r = 5
        for i in range(0, 361):
            a = m.pi * i / 180.0
            x = r * m.sin(a)
            y = r * m.cos(a)
            t.goto(x, y)
            return
    t.pencolor('black')
    a = m.pi * d / 180
    x = r * m.cos(a) + x0
    y = r * m.sin(a) + y0
    r = 10
    t.goto(x, y)
    tree(n - 1, d - 45, x, y, r * 0.7)
    t.goto(x, y)
    tree(n - 1, d + 45, x, y, r * 0.7)
    t.goto(x, y)
    return


t.setup(800, 800)
t.shape('turtle')
t.speed(10)
t.pencolor('black')

tree(10, 90, 0, 0, 100)

t.done()
