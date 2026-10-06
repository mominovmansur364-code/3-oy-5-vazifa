def juft_kvadratlar(sonlar):
    natija=[]
    for x in sonlar:
        if x%2==0:
            natija.append(x**2)
    if len(natija)==0:
        return "Juft son topilmadi"
    return natija

assert juft_kvadratlar([1, 2, 3, 4, 5])==[4,16]
assert juft_kvadratlar([1, 3, 5])=="Juft son topilmadi"
assert juft_kvadratlar([])=="Juft son topilmadi"

sonlar=list(map(int,input().split()))
print(juft_kvadratlar(sonlar))