data_kariawan = [
    {
    "nama" : "tono",
    "tanggal_lahir" : "2000",
    "gaji" : 8000000,
    },
    {
    "nama" : "siska",
    "tanggal_lahir" : "1997",
    "gaji" : 8000000,
    },
    {
    "nama" : "budi",
    "tanggal_lahir" : "1966",
    "gaji" : 10000000,
    },
    {
    "nama" : "anwar",
    "tanggal_lahir" : "1966",
    "gaji" : 8000000,
    },
]

# Void
def template_print(nama,gaji,usia = 3):
    print(f"Nama : {nama}")
    print(f"Gaji : {gaji}")
    print(f"Usia : {usia} Tahun")
    print("=======================")
# Non Void
def rumus_usia(tahun_lahir:int):
    tahun_sekarang = 2026
    usia = tahun_sekarang - int(tahun_lahir)
    return usia

data_kariawan[0]["usia"] = rumus_usia(data_kariawan[0]["tanggal_lahir"])
data_kariawan[1]["usia"] = rumus_usia(data_kariawan[1]["tanggal_lahir"])
data_kariawan[2]["usia"] = rumus_usia(data_kariawan[2]["tanggal_lahir"])
data_kariawan[3]["usia"] = rumus_usia(data_kariawan[3]["tanggal_lahir"])


print("=====Data Kariawan=====")
template_print(data_kariawan[0]["nama"],data_kariawan[0]["gaji"],data_kariawan[0]["usia"])
template_print(data_kariawan[1]["nama"],data_kariawan[1]["gaji"],data_kariawan[1]["usia"])
template_print(data_kariawan[2]["nama"],data_kariawan[2]["gaji"],data_kariawan[2]["usia"])
template_print(data_kariawan[3]["nama"],data_kariawan[3]["gaji"],data_kariawan[3]["usia"])

