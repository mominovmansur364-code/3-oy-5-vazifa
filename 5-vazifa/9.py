def ortacha(ballar):
    if len(ballar)==0:
        return "Ballar yo'q"
    return sum(ballar)/len(ballar)
assert ortacha([60, 80]) == 70.0
assert ortacha([]) == "Ballar yo'q"

scores=list(map(int,input().split()))
print(ortacha(scores))