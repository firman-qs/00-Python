import datetime as dt

# Data
data_mahasiswa = {

}

# Penomoran
no = 1

# Program
while True:
    print(f'''
Selamat datang di Pusat Data !
1. Tampilkan Data
2. Tambahkan Data
3. Hapus Data
4. Stop Program''')

    action = input('Masukkan Pilihan : ')

    if action == '1':
        print(f'{" Data Mahasiswa ".center(56, "=")}')
        print(f"{'No':^3}{'Nama':^20}{'NIM':^12}{'SKS':^4}{'beasiswa':^4}{'lahir':^10}")
        print('-' * 56)

        for mahasiswa in data_mahasiswa:

            nama = data_mahasiswa[mahasiswa]['nama']
            nim = mahasiswa
            sks = data_mahasiswa[mahasiswa]['sks']
            beasiswa = data_mahasiswa[mahasiswa]['beasiswa']
            lahir = data_mahasiswa[mahasiswa]['lahir'].strftime("%x")

            print(f"{no:^3}{nama:^20}{nim:^12}{sks:^4}{beasiswa:^4}{lahir:^10}")

            no += 1


    elif action == '2':
        nama = input("Nama : ")
        nim = input("NIM : ")
        sks = input("SKS : ")
        beasiswa = input("Beasiswa : ")

        ilahir = input("Lahir (dd-mm-yyyy): ")
        lahir = dt.datetime(int(ilahir[6:10]),int(ilahir[3:5]),int(ilahir[0:2]))

        data_mahasiswa.update({
            nim : {
                'nama' : nama,
                'sks' : sks,
                'beasiswa' : beasiswa,
                'lahir' : lahir
            }
        })

    elif action == '4':
        break