common = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weak = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

year = 2000
dan = 3
day = 0

for i in range(1, year + 1):
    day += 365
    x = 0 if i % 4 != 0 | (i % 100 == 0 and i % 400 != 0) else 1
    if x == 1:
        day += 1

w = day % 7

x = 0 if year % 4 != 0 | (year % 100 == 0 and year % 400 != 0) else 1
if x == 0:
    print(weak[w])
else:
    print(weak[w - 1])

