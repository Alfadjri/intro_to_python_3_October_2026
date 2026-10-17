x = 3
y = 2

# Penjumlahan
hasil = x + y
print(f"Hasil dari {x} + {y} = {hasil}") 
# Pengurangan
hasil = x - y
print(f"Hasil dari {x} - {y} = {hasil}")
# Perkalian
hasil = x * y
print(f"Hasil dari {x} * {y} = {hasil}")
# Pembagian
hasil = x / y
print(f"Hasil dari {x} / {y} = {hasil}") 
hasil = int(x / y)
print(f"Hasil dari Casting {x} / {y} = {hasil}")
hasil = x // y
print(f"Hasil dari Casting {x} // {y} = {hasil}") 
# Modulus (sisa dari pembagian)
hasil = x % y
print(f"Hasil dari {x} % {y} = {hasil}")
# Formula persentase
nilai_bagi = 10
nilai_total = 40
persentase = ((nilai_bagi / nilai_total) * 100)
print(f"Persentase : {int(persentase)}%")

# persentase = persentase + 1
persentase += 1
print(f"Persentase : {int(persentase)}%")
persentase -= 1
print(f"Persentase : {int(persentase)}%")