import math

p = math.pi

for i in range(0, 361):
    a = p * i / 180.0
    s = 300 * math.sin(a)
    print(i, s)
