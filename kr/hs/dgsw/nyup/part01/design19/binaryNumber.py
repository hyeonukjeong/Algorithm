def f(n, s):
    if n == 0:
        print(s)
        return
    f(n -1, s + '0')
    f(n -1, s + '1')
    return

f(5, '')
