def collatz(num):
    cycle = 1
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        cycle += 1
    return cycle

def col_range(n1, n2):
    col_num = 0
    if n1 > n2:
        n1, n2 = n2, n1
    for i in range(n1, n2+1):
        if col_num < collatz(i):
            col_num = collatz(i)
    return col_num

print(col_range(999999, 1))
