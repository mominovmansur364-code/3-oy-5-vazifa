def xavfsiz_bolish(a, b):
    if b==0:
        return "0 ga bo'lish mumkin emas!"
    return a/b
son1,son2=map(int,input("Ikkita son kiriting: ").split())
print(xavfsiz_bolish(son1,son2))
    