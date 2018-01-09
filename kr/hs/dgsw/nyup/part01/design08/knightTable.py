# 기사의 수
knight = 12
# 기사의 수를 2진수화
b_knight = bin(knight)
# 생존 기사의 자리
k_position = int(b_knight[3:] + b_knight[2], base = 2)
# 출력
print(k_position)
