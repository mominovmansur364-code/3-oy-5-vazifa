def chegirmali_narxlar(narx_matnlari, chegara):
    if chegara < 0:
        raise ValueError("Chegara manfiy bo'lishi mumkin emas")

    f_narxlar = filter(lambda narx: narx.isdigit(), narx_matnlari)

    ch_narxlar = [int(narx) - 2000 for narx in f_narxlar if int(narx) >= chegara]

    return ch_narxlar


assert chegirmali_narxlar(["9000", "10000", "15000", "x"], 10000) == [8000, 13000]
assert chegirmali_narxlar([], 10000) == []

try:
    chegirmali_narxlar(["10000"], -1)
except ValueError as e:
    assert str(e) == "Chegara manfiy bo'lishi mumkin emas"


narxlar = input("Narxlarni kiriting: ").split()
chegara = int(input("Chegarani kiriting: "))
print(chegirmali_narxlar(narxlar, chegara))