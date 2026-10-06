def musbatlarni_ajrat(sonlar):
    natija=[]
    for x in sonlar:
        if x>0:
            natija.append(x)

    return natija

assert musbatlarni_ajrat([-5, 10, 0, 25, -3])==[10,25]
assert musbatlarni_ajrat([])==[]
assert musbatlarni_ajrat([-5,-6,-2,0])==[]

sonlar=list(map(int,input().split()))
print(musbatlarni_ajrat(sonlar))