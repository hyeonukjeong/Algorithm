def euclid(n, m):
    if m == 0:
        return n
    return euclid(m, n % m)

gcd = euclid(123456789, 987654321)
print(gcd)