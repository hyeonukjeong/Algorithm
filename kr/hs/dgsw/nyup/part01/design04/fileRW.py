# 입력 파일 경로
fin = open('./input.txt')
fout = open('./output.txt','w')
# 1줄씩 읽기
a = fin.readline()
b = fin.readline()
c = fin.readline()
w = '{0:s} {1:s} {2:s}'.format(a, b, c)
# 출력
print("a가 가져간 금화의 수 :", a)
print("b가 가져간 금화의 수 :", b)
print("c가 가져간 금화의 수 :", c)
fout.write(w)
# 파일 닫기
fin.close()
fout.close()