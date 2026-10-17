
# Kondisi if
# if kondisi:
#  aksi
nilai = 70
print("====if====")
if nilai > 70:
    print("Kamu lulus")
print("====if else ====")
if nilai > 70:
    print("Kamu lulus")
else:
    print("Kamu tidak lulus")
print("====if tenery ====")
nilai = 70
hasil = "Kamu lulus" if nilai > 70 else "Kamu tidak lulus"
print(hasil)
print("====if elif else ====")
nilai = 75
if nilai > 90:
    print("Kamu lulus dengan predikat A")
elif nilai > 80 and nilai <= 90 :
    print("Kamu lulus dengan predikat B")
elif nilai > 70 and nilai <= 80:
    print("Kamu lulus dengan predikat C")
elif nilai > 60 and nilai <= 70:
    print("Kamu lulus dengan predikat D")
else:
    print("Kamu Drop Out")


# match and case
print("====match and case====")
print("=====Menu=====")
print("1. Menu 1")
print("2. Menu 2")
print("3. Exit")
select = input("Pilih menu : ")
match select:
    case "1":
        print("Kamu memilih menu 1")
    case "2":
        print("Kamu memilih menu 2")
    case "3":
        print("Kamu memilih menu Exit")
    case _:
        print("Menu tidak tersedia")
# try and catch
print("====try and catch====")
try:
    angka = int(input("Masukkan angka : "))
    print(f"Angka yang kamu masukkan adalah {angka}")
except ValueError:
    print("Kamu harus memasukkan angka")