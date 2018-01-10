n, sum = 2, 1
while n != sum:
    n += 1
    sum += str(n).count('1')
print(n)
