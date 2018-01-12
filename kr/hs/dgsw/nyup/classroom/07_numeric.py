#  1  2  5  6  9 10
#  3  4  7  8 11 12
# 13 14 17 18 21 22
# 15 16 19 20 23 24


for i in range(1, 14, 12):
    print('\n')
    for j in range(i, i + 3, 2):
        print('\n')
        for k in range(j, j + 9, 4):
            print(end=' ')
            for l in range(k, k + 2, 1):
                if l < 10:
                    print('', l, end=' ')
                else:
                    print(l, end=' ')
