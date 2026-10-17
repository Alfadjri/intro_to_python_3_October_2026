import datetime as date
tanggal = date.datetime.now()
manger = "Gea Saskia"
pt = "PT.Ruang Keahlian"
alamat = "Jakarta Timur"

# String Formating Posisional 
print("==========Posisional==========")
print("\t\t{0}\nYth.{1}\nManager SDM {2}\n{3}".format(tanggal,pt,manger,alamat))
# String Formating Keyword
print("==========Keyword==========")
print("\t\t{tanggal}\nYth.{manger}\nManager SDM {pt}\n{alamat}".format(tanggal=tanggal, pt=pt, manger=manger, alamat=alamat))
# String Fromating Shorcut
print("==========Shorcut==========")
print(f"\t\t{tanggal}\nYth.{manger}\nManager SDM {pt}\n{alamat}")