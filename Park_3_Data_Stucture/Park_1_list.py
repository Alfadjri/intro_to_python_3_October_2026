# CRUD
# C (Create)
# inisialisasi data
data_makanan = ["Nasi Goreng", "Mie Goreng", "Sate Ayam", "Bakso","Ayam"]
# Add data (append)
data_makanan.append("Soto Ayam")
# R (Read)
print(f"All Data : {data_makanan}")
data_makanan.append("Soto Lamongan")
print(f"All Data : {data_makanan}")
data_makanan.append(["Nasi","Semangka"])
print(f"All Data : {data_makanan}")
print(f"Data ke 5 : {data_makanan[5]}")
# U (Update)
data_makanan[7] = "Nasi"
print(f"All Data : {data_makanan}")
# D (Delete)
del data_makanan[6]
print(f"All Data : {data_makanan}")