# 입력 파일 경로
fin = open('./input.txt')
# 1줄씩 읽기
a = int(fin.readline())
b = int(fin.readline())
c = int(fin.readline())
# 출력
print("a가 가져간 금화의 수 :", a)
print("b가 가져간 금화의 수 :", b)
print("c가 가져간 금화의 수 :", c)
# 파일 닫기
fin.close()