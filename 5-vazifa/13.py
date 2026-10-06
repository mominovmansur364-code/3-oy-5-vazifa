def yoshlarni_ol(yosh_matnlari):
    natija=[]
    for x in yosh_matnlari:
        try:
            natija.append(int(x))
        except:
            print(f"Notogri yosh: {x}")
    return natija

yoshlar=input().split()
print(yoshlarni_ol(yoshlar))
    