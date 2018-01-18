def part(count, n, k, s):
    if n < 0:
        return
    elif n == 0:
        print(s[1:])
    else:
        for i in range(1, k + 1):
            count += 1
            part(count, n - i, i, s + '+' + str(i))
    return count

n = int(input('몇의 분할 수를 구할까요? '))
print(n, '은', part(0, n, n, ''), '가지의 분할 수가 있습니다.')
