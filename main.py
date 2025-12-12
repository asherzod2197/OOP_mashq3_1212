# 5
class BankHisob:
    def __init__(self, egasi, balans):
        self.egasi = egasi
        self.__balans = balans

    def balansni_kor(self):
        return f"{self.egasi}ning balansi: {self.__balans}"

    def pul_qosh(self, miqdor):
        if miqdor > 0:
            self.__balans += miqdor
            return f"{miqdor} so`m qoshildi."
        return "Xato: Miqdor Musbat bo'lishi kerak!"

hisob = BankHisob('Olim', 10000)
print(hisob.balansni_kor())

print(hisob.pul_qosh(555))
print(hisob.balansni_kor())
