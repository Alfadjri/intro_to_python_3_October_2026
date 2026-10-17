# For 
# for index sementara in data : 
    # nilai yang mau di ulang
# Range(Start , Stop , Step)
print("=====For Loop=====")
for value in range(1,11):
  print(f"Index ke : {value}")

# yang di loop list
print("=====For Loop using list=====")
makanan = ['Nasi Goreng', 'Mie Goreng', 'Sate Ayam', 'Bakso', 'Ayam', 'Soto Ayam', 'Soto Lamongan', 'Nasi']
for value in makanan:
    print(f"Makanan : {value}")
print("======While Loop======")
# While loop
# Saat kita tau kapan kita berhenti tapi tau jalan atau start nya di mana 
nomor = 11
while nomor <= 10:
    print(f"Index of : {nomor}")
    nomor += 1

print("====break and continue====")
nomer = 1
while nomer <= 100:
    if nomer % 2 == 0 : 
        nomer += 1
        continue

    if nomer >= 20 :
        nomer += 1
        break

    print(f"Index of {nomer}")
    nomer += 1