# 나이가 같은 부부가 있는데 9명의 자녀가 있으며,터울이 같다. 올해는 자녀의 나이를 제곱해서 합한것이 부부 나이를 제곱한것과 같다. 인간 수명은 200살 이하이다. 인간은 최소 1살 이상이다.

max_age = 200
kids = 9
pow_arr = []
n = 0

for i in range(0, max_age + 1):
    pow_arr.append(i * i)

for i in range(1, max_age + 1):
    for j in range(1, max_age + 1):
        s = 0
        for k in range(0, kids):
            a = i + j * k
            s += a * a
        n += s in pow_arr
print("총", n, "회")