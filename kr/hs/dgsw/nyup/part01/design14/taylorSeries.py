eps, s, sum = 1000000, 1, 0

for n in range(1, eps + 1):
    sum += s / n
    s = -s

print(sum)