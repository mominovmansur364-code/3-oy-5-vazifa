def narxni_hisobla(narx_matnlari, chegirma):
    if chegirma<0 or chegirma>100:
        raise ValueError("Chegirma 0 va 100 oralig'ida bo'lishi kerak")
    natija=[]
    for x in narx_matnlari:
        try:
            narx=int(x)
            yakuniy_narx=narx-(narx*chegirma/100)
            natija.append(yakuniy_narx)
        except ValueError:
            print(f"Noto'g'ri narx: {x}")

    return natija

assert narxni_hisobla(["10000", "20000", "abc"], 10) == [9000.0, 18000.0]
assert narxni_hisobla([], 20) == []

try:
    narxni_hisobla(["10000"], 150)
except ValueError as e:
    assert str(e) == "Chegirma 0 va 100 oralig'ida bo'lishi kerak"
