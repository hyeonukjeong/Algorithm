def rangeOf0(m):
    count = 0
    for i in range(1, m + 1):
        if i % 5 == 0:
            count += 1
            if i % 25 == 0:
                count += 1
    return count

print(rangeOf0(100))
