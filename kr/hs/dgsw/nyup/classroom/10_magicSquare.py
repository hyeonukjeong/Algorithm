def magicSquare(n):
    i = 1
    j = (n + 1) // 2
    m = [[0] * n for i in range(1, n + 1)]
    m[i - 1][j - 1] = 1

    for k in range(2, n * n):
        if (k - 1) % n == 0:
            i += 1

        elif i == 1:
            i = n
            j += 1

        elif j == n:
            i -= 1
            j = 1

        else:
            i -= 1
            j += 1

        m[i-1][j-1] = k

    for k in m:
        print(k)

size = int(input("어느 크기의 마방진을 만들까요? "))

magicSquare(size)
