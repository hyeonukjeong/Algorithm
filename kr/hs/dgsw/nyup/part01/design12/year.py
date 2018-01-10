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

# 평년, 윤년
year = ['common', 'leap']
# 연도를 100으로 나눈 나머지
years = y % 100
# 인덱스 값 0으로 세팅
x = 0
# 연도를 100으로 나눈 나머지의 값이 4로 나머지가 0이 되게 나누어 진다면
if years % 4 == 0:
# 인덱스 값 1로 세팅
    x = 1
#출력
print(year[x])
