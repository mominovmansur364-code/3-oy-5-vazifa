def otgan_ballar(ballar):
    return [b for b in ballar if b>=60]

assert otgan_ballar([59, 60, 75, 40]) == [60, 75]
assert otgan_ballar([60]) == [60]                  
assert otgan_ballar([]) == []

ballar_listi=list(map(int,input().split()))

print(otgan_ballar(ballar_listi))
