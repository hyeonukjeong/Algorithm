def big(n):
    print('')
    for i in range(n):
        for j in range(n):
            a = (' ', '❄︎')[j == 0 or j == n - 1 or j == i]
            print(a, end='')
        print('')

big(3)

import turtle as t

def turtleBig(n):
    t.setup(800, 800)
    t.ht()
    t.speed(10)
    t.dot_distance = 25
    t.penup()
    t.goto(-t.dot_distance * n, t.dot_distance * n)

    for i in range(n):
        for j in range(n):
            (t.forward(t.dot_distance), t.dot())[j == 0 or j == n - 1 or j == i]
        t.goto(-t.dot_distance * n, t.dot_distance * n)

    print('complete')
    t.done()

turtleBig(3)
