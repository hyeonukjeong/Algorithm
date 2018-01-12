di = (0, 1, 1, 1, 0, -1, -1, -1)
dj = (1, 1, 0, -1, -1, -1, 0, 1)

n = 10

next = [[0] * (n + 2) for i in range(n + 2)]
now = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for loop in range(10):
    for i in range(n + 2):
        for j in range(n + 2):
            if now[i][j] == 0:
                print(' %s ' %'🍀', end=' ')
            else:
                print(' %s ' %'🐰', end=' ')
        print('')
        print('')
    print('')

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            s = 0
            for k in range(8):
                s += now[i + di[k]][j + dj[k]]
            life = (now[i][j] == 1 and (s == 2 or s == 3)) or (now[i][j] == 0 and s == 3)
            next[i][j] = 1 if life else 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            now[i][j] = next[i][j]
