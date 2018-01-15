info_input = '''a 8.32 9.42 9.02 8.80 9.24
b 9.11 7.45 8.83 9.12 9.41
c 8.87 9.12 9.48 8.34 9.66
d 9.03 8.96 9.52 9.02 8.95
e 8.87 9.28 9.73 8.37 9.01'''

player_a = info_input[0:26].split()
player_b = info_input[27:53].split()
player_c = info_input[54:80].split()
player_d = info_input[81:107].split()
player_e = info_input[108:134].split()

a = player_a[1:6]
b = player_b[1:6]
c = player_c[1:6]
d = player_d[1:6]
e = player_e[1:6]

print(a)
print(b)
print(c)
print(d)
print(e)
