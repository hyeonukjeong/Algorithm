di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)

row, col = 6, 10

a = [[-1] * (col + 2) for i in range(row + 2)]

for i in range(1, row + 1):
    for j in range(1, col + 1):
        a[i][j] = 0

i, j, dir = 1, 1, 0

for k in range(1, row * col + 1):
    a[i][j] = k
    fi = i + di[dir]
    fj = j + dj[dir]
    if a[fi][fj] != 0:
        dir = (dir + 1) % 4
    i += di[dir]
    j += dj[dir]

for i in range(1, row + 1):
    for j in range(1, col + 1):
        print('%4d' %a[i][j], end='')
    print('')