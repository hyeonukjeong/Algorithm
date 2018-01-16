def f1(n):
    global s
    if n == 0:
        return 0
    s += n
    f1(n - 1)
    return s

def f2(n):
    if n == 0:
        return 0
    s = n + f2(n - 1)
    return s

def f3(n):
    if n == 0:
        return 0
    return n + f3(n - 1)

def f4(n):
    if n <= 0:
        return 0
    return n + (n - 1) + f4(n - 2)

s = 0
print(f1(10))
print(f2(10))
print(f3(10))
print(f4(10))
