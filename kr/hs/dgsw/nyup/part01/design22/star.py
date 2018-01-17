import turtle as t

t.setup (800, 800)
t.speed(5)
t.pencolor('red')
t.width(5)

for i in range(5):
    t.fd(300)
    t.lt(144)

for i in range(5):
    t.fd(200)
    t.lt(144)
    t.fd(200)
    t.rt(72)

t.done()
