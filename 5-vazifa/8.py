def narxlarni_ol(narx_matnlari):
    natija=[]
    for x in narx_matnlari:
        try:
            natija.append(int(x))
        except:
            print(f"Notogri narx: {x}")
    return natija

narxlar=input().split()
print(narxlarni_ol(narxlar))