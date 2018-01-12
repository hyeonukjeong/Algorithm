common = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weak = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

year = 2000
dan = 3
day = 0

def cl_function(n):
    x = 0 if n % 4 != 0 | (n % 100 == 0 and n % 400 != 0) else 1

for i in range(1, year + 1):
    day += 365
    if cl_function(i) == 1:
        day += 1

w = day % 7

if cl_function(year) == 0:
    print(weak[w])
else:
    print(weak[w - 1])
