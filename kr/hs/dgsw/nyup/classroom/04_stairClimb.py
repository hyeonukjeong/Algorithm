# 계단의 수
stair = 10
# 올라가는 방법의 수
way = 0


def stairClimb(stair):
    prev, cur = 0, 1
    for i in range(stair):
        prev, cur = cur, prev + cur
    return cur

def climbStair(stair):
    if stair == 0:
        way = 0
    elif stair == 1:
        way = 1
    else:
        way = stairClimb(stair - 1) + stairClimb(stair - 2)
    print("계단을 올라가는 방법은", way, "가지 입니다.")

climbStair(stair)
