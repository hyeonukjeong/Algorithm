row = 15

f = [1]

for i in range(1, row + 1):
    f.append(i * f[i - 1])
for j in range(row + 1):
    print(' ' * 3 * (row - j), end='')
    for k in range(j + 1):
        l = f[j] // (f[k] * f[j - k])
        if l % 2 != 0:
            print('%6d' %l, end='')
        else:
            print('      ', end='')
    print('')
