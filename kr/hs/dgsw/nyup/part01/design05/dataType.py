a = '''Hello
    My
        name
            is
                Jeong
                    Hyeon
                        Uk
                            !!'''

print(a)

b = 'Abcdef'

print(b)
print(b[2])
print(b[3:5])
print(b[3:])
print(b[:])

c = [1, 5, 'a', [3, 7]]

print(c)
print(c[2])
print(c[3][1])

d = range(10)

print(d)
for i in d:
    print(i)

e = range(5, 12, 2)

for i in e:
    print(i)

f = range(9, -4, -3)

for i in f:
    print(i)

g = {65:'A', 66:'B'}

print(g[66])

h = {5, 8}

print(type(h))

i = {5:8}

print(type(i))

j = {}

print(j)

k = set({})

print(k)

l = frozenset({})

print(l)

m = {1, 3, 3, 3, 2}

print(m)