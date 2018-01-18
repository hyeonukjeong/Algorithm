def perm(r, s):
    if r <= 0:
        print(s)
    else:
        for i in range(1, n + 1):
            perm(r - 1, s + str(i))
    return

n = 3
r = 4
perm(r, '')
