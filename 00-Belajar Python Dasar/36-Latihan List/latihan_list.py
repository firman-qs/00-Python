"""Docstring"""
import os
os.system("cls")

daftar_buku = []
while True:
    print(f"""{90*"#"}\n{f"{36*' '}Perpustakaan{36*' '}".center(90,"#")}\n{90*"#"}\n\nMenu:
1. Tambahkan Buku\t2. Tampilkan Buku\t3. Hapus Buku""")

    action = input("\nMasukkan pilihan: ")
    # Masukkan buku
    if action == "1":
        while True:
            nama_buku = input("Nama buku\t: ")
            nama_pengarang = input("Pengarang\t: ")
            tahun_terbit = str(input("Tahun terbit\t: "))
            daftar_buku.append([nama_buku, nama_pengarang, tahun_terbit])
            # tambahkan lagi atau tidak
            lanjut = input("Tambahkan lagi? ").lower()
            if lanjut in ["n", "no"]:
                break

    # Menampilkan buku
    elif action == "2":
        os.system("cls")
        print(f'''{90*"="}\nNo.\t{"judul".center(30)}{"penulis".center(30)}{"tahun".center(30)}
{90*"-"}''')

        for index, buku in enumerate(daftar_buku):
            print(
                f"{index+1}.\t{buku[0].ljust(30)}{buku[1].ljust(30)}{buku[2].ljust(30)}")
        print(f"{90*'='}")
        print("\n"*1)

    # Menghapus Buku
    elif action == "3":
        hapus_buku = int(input("Nomor buku yang akan dihapus: "))
        del daftar_buku[hapus_buku-1]
        print(f"Buku dengan no {hapus_buku} berhasil dihapus")
