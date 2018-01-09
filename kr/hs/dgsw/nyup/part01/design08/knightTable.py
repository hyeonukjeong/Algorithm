# 기사의 수
knight = 12
# 기사의 수를 2진수화
b_knight = bin(knight)
# 생존 기사의 자리
k_position = int(b_knight[3:] + b_knight[2], base = 2)
# 출력
print(knight, "명의 기사가 있을때 생존 기사의 자리는", k_position, "번째 자리입니다.")
# 로그를 사용하기 위해 참조
from math import log
# 기사의 수
m_knight = 12
# 생존 기자의 자리
m_k_position = (m_knight - 2 ** int(log(m_knight, 2))) * 2 + 1
# 출력
print(m_knight, "명의 기사가 있을때 생존 기사의 자리는", m_k_position, "번째 자리입니다.")
