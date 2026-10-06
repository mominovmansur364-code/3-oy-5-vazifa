def ballni_tekshir(ball):
    if ball<0 or ball>100:
        raise ValueError("Ball 0 dan 100 gacha bo'lishi kerak")
    return ball

score=int(input())
print(ballni_tekshir(score))