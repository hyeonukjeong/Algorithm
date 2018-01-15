def taxi(k):
    f = k * 500
    return f
fare = taxi(4)
print(fare)

def hi():
    print('Hello')
hi()

def hi():
    return 'Hello'
print(hi())

def calc(a, b, c):
    return a - b + c
s = calc(1, 2, 3) + 4
print(s)

def calc(a = 1, b = 2, c = 3):
    return a - b + c
s = calc() + 4
print(s)

def calc(a, b, c):
    return a - b + c
s = calc(b = 2, c = 3, a = 1) + 4
print(s)

def calc(a, b, c):
    p = a - b + c
    q = a * b + c
    x = [p, q]
    return x
y = calc(1, 2, 3)
print(y[0], y[1])

def calc(*args):
    x = sum(args)
    return x
y = calc(1, 2, 3)
print(y)
