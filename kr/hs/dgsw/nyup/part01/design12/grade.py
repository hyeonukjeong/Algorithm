score = 100

if score >= 90:
    grade = 'A'
elif 90 > score >= 80:
    grade = 'B'
elif 80 > score >= 70:
    grade = 'C'
else:
    grade = 'F'

print(grade)

g = 'FFFFFFFCBA'

grade = g[score//10]

print(grade)
