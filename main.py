# Program Python sederhana: Kalkulator penjumlahan
def tambah(angka1, angka2):
    return angka1 + angka2

if __name__ == "__main__":
    print("Selamat datang di kalkulator penjumlahan!")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    hasil = tambah(angka1, angka2)
    print(f"Hasilnya adalah: {hasil}")
