def numDia(n):
    for i in range(1, n + 1):
        m = (n + 1) // 2
        t = m - abs(i - m)
        for j in range(1, t + 1):
            print('%3d' %i, end=' ')
        print('')

numDia(9)