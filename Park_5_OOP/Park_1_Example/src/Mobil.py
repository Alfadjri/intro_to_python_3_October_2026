class Mobil:
    # Object
    merek = "default"
    tipe_mobil = "default"
    warna = "default"
    # Property
    veleg = "T34" # public
    _cc_mobil = 1500 #private
    __kursi = "Abu-abu" #protected

    # Constructor
    def __init__(self,merek,tipe_mobil,warna):
        self.merek = merek
        self.tipe_mobil = tipe_mobil
        self.warna = warna
    # Method atau fungsi
    def getProfile(self):
        print(f"Merek\t\t: {self.merek}")
        print(f"Type\t\t: {self.tipe_mobil}")
        print(f"CC Mobil\t: {self._cc_mobil} cc")
        print(f"Warna\t\t: {self.warna}")
        print(f"Interior\t: {self.__kursi}")
        print(f"Veleg\t\t: {self.veleg}")
        print("===========")
