def foydalanuvchi_nomini_ol(foydalanuvchi):
    return foydalanuvchi.get("username", "Username topilmadi")

print(foydalanuvchi_nomini_ol({"username": "eshmat"}))
print(foydalanuvchi_nomini_ol({"name": "Eshmat"})) 