import json

path = r"D:\alndutndut.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

def tambah_data(kode, nama, stok, harga):
    data.append({"kode": kode, "nama": nama, "stok": stok, "harga": harga})
    return "data sudah ditambah ya ndut"

def simpan_file():
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return "tersimpan ke alndutndut.json!"

while True:
    print("\n=== sistem manajemen invetaris nih ndut ===")
    print("1. Lihat Data Barang")
    print("2. Tambah Barang")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n--- data barang nih ndut ---")
        print(data)

    elif pilihan == "2":
        kode = input("Kode barang : ")
        nama = input("Nama barang : ")
        stok = int(input("Stok        : "))
        harga = int(input("Harga       : "))
        print("\n", tambah_data(kode, nama, stok, harga))
        print("\n", simpan_file())

    elif pilihan == "3":
        print("terimakasihh sudah meenggunakann sistem ini yaa ndut")
        break

    else:
        print("pilihan ga valid nih nduttt")