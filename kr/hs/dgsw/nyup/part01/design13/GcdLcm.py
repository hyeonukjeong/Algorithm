a = 123456789
b = 987654321
t = a * b

while b != 0:
    a, b = b, a % b
gcd = a
lcm = t // gcd

print("최대공약수 :", gcd)
print("최소공배수 :", lcm)
