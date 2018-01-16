def dev(n, m):
    if (n == m):
        return a[n]
    l = (n + m) // 2
    s = dev(n, l) + dev(l + 1, m)
    return s

a = [5, 7, 9, 3, 1, 6, 4, 2, 8]
sum = dev(0, len(a) - 1)
print(sum)
