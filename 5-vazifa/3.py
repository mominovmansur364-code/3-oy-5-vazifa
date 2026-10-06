royxat=[10,20,30,78,54,63]
def elementni_ol(royxat, indeks):
    try:
        return royxat[indeks]
    except IndexError:
        return "Bunday index yoq"

index=int(input())
print(elementni_ol(royxat,index))