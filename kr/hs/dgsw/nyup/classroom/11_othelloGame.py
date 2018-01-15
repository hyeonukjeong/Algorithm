di = (0, 1, 1, 1, 0, -1, -1, -1)
dj = (1, 1, 0, -1, -1, -1, 0, 1)

size = 8

next = [[0] * size for i in range(size)]
now = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 2, 0, 0, 0],
       [0, 0, 0, 2, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0]]

for i in range(size):
    for j in range(size):
        if now[i][j] == 0:
            print(' %s ' %'+', end=' ')
        elif now[i][j] == 1:
            print(' %s ' %'●', end=' ')
        else:
           print(' %s ' %'○', end=' ')
    print('')
    print('')