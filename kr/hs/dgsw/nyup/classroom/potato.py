# 아이가 1분에 깎는 감자의 양
girl = 3
# 엄마가 1분에 깎는 감자의 양
mom = 5
# 엄마가 늦게 온 시간
difference = 4
# 전체 깎은 감자의 양
potato = 52
# 아이가 4분동안 깍은 감자의 양
g_potato = girl * difference
# 아이와 엄마가 1분에 깎는 감자의 양
co_work = girl + mom
# 아이와 엄마가 함께 깎은 감자의 양
co_potato = potato - g_potato
# 아이와 엄마가 함께 깎은 시간
co_time = co_potato / co_work
# 아이가 감자 깎은 시간
girl_time = co_time + difference
# 아이가 깎은 감자의 양
girl_potato = girl * girl_time
# 출력
print("아이는 감자", girl_potato, "개를 깎았습니다.")
