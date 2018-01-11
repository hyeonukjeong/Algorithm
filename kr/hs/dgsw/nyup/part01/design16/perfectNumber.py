maximum = 10000
perfectNumber = []

for i in range(2, maximum+1):
    sum = 0
    for j in range(1, i // 2 + 1):
        if  i % j == 0:
            sum += j
    if sum == i:
        perfectNumber.append(sum)

print(perfectNumber)
