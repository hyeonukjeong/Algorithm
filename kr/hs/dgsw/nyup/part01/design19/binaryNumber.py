n = input('몇 자리 이진수가 필요하신가요? ')
m = 0

def binFunc(n):
    if m == n:
        return m
    else:
        print(bin(m))
        return binFunc(int(n) - 1)

binFunc(n)

