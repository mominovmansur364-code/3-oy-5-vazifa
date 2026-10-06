def bonus_qosh(ball):
    return ball+5
assert bonus_qosh(70)==75
assert bonus_qosh(0)==5

score=int(input())
print(bonus_qosh(score))