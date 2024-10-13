# 1-misol
class Odam:
    def __init__(self, ism):
        self.ism = ism

    def salomlashish(self):
        print(f"Salom {self.ism}!")

ism = input("Ismingizni kiriting: ")
odam = Odam(ism)
odam.salomlashish()

# 2-misol
"""
class Odam:
    def __init__(self, ism):
        self.ism = ism

    def kuylash(self):
        print(f"{self.ism} kuylamoqda...")

    def eshitish(self, boshqa_odam):
        print(f"{self.ism} {boshqa_odam.ism}ning kuyini eshitdi.")

    def gapirish(self):
        print(f"{self.ism}: Ajoyib kuy ekan!")


odam1 = Odam("Ali")
odam2 = Odam("Vali")


odam1.kuylash()
odam2.eshitish(odam1)
odam2.gapirish()
"""
# 3-misol
"""
import time

class Odam:
    def __init__(self, ism):
        self.ism = ism

    def yugurish(self):
        print(f"{self.ism} yugurishni boshladi...")
        time.sleep(5)  
        self.yiqilish()

    def yiqilish(self):
        print(f"{self.ism} yiqilib tushdi.")


odam = Odam("Javohir")
odam.yugurish()
"""
# 4-misol
"""
class Odam:
    def __init__(self, ism):
        self.ism = ism

    def tepish(self, koptok):
        print(f"{self.ism} koptokni tepti.")
        koptok.uchish()

class Koptok:
    def uchish(self):
        print("Koptok uchmoqda...")

    def ochish(self):
        print("Koptok ochmoqda...")
zokir = Odam("Zokir")
koptok = Koptok()

zokir.tepish(koptok)
"""
# 5-misol
"""
class Vaqt:
    def __init__(self, soat, minut, sekund):
        self.soat = soat
        self.minut = minut
        self.sekund = sekund

    def vaqtni_chiqarish(self):
        print(f"{self.soat:02d}:{self.minut:02d}:{self.sekund:02d}")

class Hour:
    def oshirish(self, vaqt):
        vaqt.soat = (vaqt.soat + 5) % 24  # 24 soat ichida qaytarib olish

class Minut:
    def oshirish(self, vaqt):
        vaqt.minut = (vaqt.minut + 5) % 60  
class Sekund:
    def oshirish(self, vaqt):
        vaqt.sekund = (vaqt.sekund + 5) % 60  

vaqt = Vaqt(23, 58, 57)
print("Dastlabki vaqt:")
vaqt.vaqtni_chiqarish()


hour = Hour()
minut = Minut()
sekund = Sekund()

hour.oshirish(vaqt)
minut.oshirish(vaqt)
sekund.oshirish(vaqt)

print("O'zgartirilgan vaqt:")
vaqt.vaqtni_chiqarish()
"""
