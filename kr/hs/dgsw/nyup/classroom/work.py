# a, b 같이 일한 날
co_work = 4
# a 혼자 일한 날
a_work = 1
# c가 지불하는 돈
c_money = 90000
# 전체 일한 날
work = co_work * 2 + a_work
# 원래 일해야 하는 날
default_work = work / 3
# a가 일한 날
a = co_work + a_work
# b가 일한 날
b = co_work
# a가 c를 대신한 일의 날
ac = a - default_work
# b가 c를 대신한 일의 날
bc = b - default_work
# a가 받아야 하는 돈
a_money = c_money * ac / default_work
# b가 받아야 하는 돈
b_money = c_money * bc / default_work
# 출력
print("a는", a_money, "원, b는", b_money, "원을 받아야 합니다.")
