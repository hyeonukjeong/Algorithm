def f(n):
    if n == 0:
        return
    f(n - 1)
    print(n, end=' ')
    return

f(10)

def add(n, m):
    if n == 0:
        return
    add(n - 1, m + n)

s = add(10, 0)
print(s)
