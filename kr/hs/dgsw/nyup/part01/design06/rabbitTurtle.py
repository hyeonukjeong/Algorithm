# 토끼의 속도
rabbit = 9
# 거북이의 속도
turtle = 2
# 토끼와 거북이 사이의 거리
distance = 99
# 토끼가 간 거리
r_distance = rabbit * distance / (rabbit + turtle)
# 거북이가 간 거리
t_distance = turtle * distance / (rabbit + turtle)
# 출력
print("토끼는", r_distance, "km, 거북이는", t_distance, "km 왔습니다.")