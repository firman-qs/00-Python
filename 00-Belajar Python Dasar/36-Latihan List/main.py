# latihan list
# daftar buku
# hapus buku beloem ada

daftar_buku = []
while True:
    title = " Perpustakaan ".center(77,"=")
    print(f"""

{title}
1. Tambahkan buku
2. Tampilkan Buku
3. Hapus Buku""")
    action = input("Masukkan pilihan: ")

    if action == "1":
        while True: 
            title = " input Buku ".center(77,"~")
            print(title)
            
            buku = input("Nama Buku: ")
            pengarang = input("Nama Pengarang: ")
            tahun = input("Tahun: ")
            buku_baru = [buku,pengarang,tahun]
            daftar_buku.append(buku_baru)
            
            lanjut = input("Tambahkan lagi? (y/n): ")
            if lanjut == "n":
                break

    if action == "2":
        title = " Daftar Buku ".center(77,"~")
        print(f"\n{title}")
        
        print(f"No.\t| Nama\t\t\t\t| Pengarang\t       | Tahun      |")
        
        for index,buku in enumerate(daftar_buku):
            print(f"{index+1}\t|{buku[0]:>30} | {buku[1]:>20} | {buku[2]:>10} |")
