# 1-misol
class Talaba:
    def __init__(self, ism, familiya, kurs, universitet):
        self.ism = ism
        self.familiya = familiya
        self.kurs = kurs
        self.universitet = universitet

    def get_fullname(self):
        return f"{self.ism} {self.familiya}"

    def get_info(self):
        print(f"Ism: {self.ism}")
        print(f"Familiya: {self.familiya}")
        print(f"Kurs: {self.kurs}")
        print(f"Universitet: {self.universitet}")


talaba1 = Talaba("Azamat", "Tojiyev", 3, "Toshkent Davlat Universiteti")

print(talaba1.get_fullname())

talaba1.get_info()

class Kitob:
    def __init__(self, nomi, muallif, sahifa_soni, narxi):
        self.nomi = nomi
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni
        self.narxi = narxi

    def get_summary(self):
        return f"{self.nomi}, {self.muallif} va {self.sahifa_soni} sahifadan iborat"

    def is_expensive(self, limit):
        if self.narxi > limit:
            return "Qimmat"
        else:
            return "Arzon"



kitob1 = Kitob("Python Programming", "Mark Lutz", 1200, 450000)

print(kitob1.get_summary())

print(kitob1.is_expensive(300000))
print(kitob1.is_expensive(500000))
