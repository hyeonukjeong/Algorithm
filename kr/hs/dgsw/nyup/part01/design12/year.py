# 연도
y = 2000

# 평년, 윤년
year = ['common', 'leap']
# 평년, 윤년 구분
x = 0 if y % 4 != 0 | (y % 100 == 0 and y % 400 != 0) else 1
# 출력
print(year[x])

# 윤년, 평년
year = ['leap', 'common']
# 논리 연산
x = y % 4 != 0 | (y % 100 == 0 and y % 400 != 0)
# 출력
print(year[x])

# 윤년, 평년
year = ['common', 'leap']
# 논리 연산
x = (y % 4 == 0 and y % 100 != 0) | y % 400 == 0
# 출력
print(year[x])
