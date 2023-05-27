""" Latihan Dictionary Part a"""
import datetime as dtm
import os
import string
import random

# template dictionary mahasiswa
mahasiswa_template = {
    "nama": "nama",
    "nim": "00000000",
    "sks_lulus": 0,
    "lahir": dtm.date(1111, 11, 1)
}

data_mahasiswa = {}

os.system("cls")
while (True):
    print(f"{'SELAMAT DATANG':^51}")
    print(f"{'DATA MAHASISWA':^51}")
    print(51*"-")

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa["nama"] = input("Nama Mahasiswa: ")
    mahasiswa["nim"] = input("NIM Mahasiswa: ")
    mahasiswa["sks_lulus"] = input("SKS Lulus: ")
    TAHUN = int(input("Tahun Lahir: "))
    BULAN = int(input("Bulang Lahir: "))
    HARI = int(input("Hari Lahir: "))
    mahasiswa["lahir"] = dtm.date(TAHUN, BULAN, HARI)

    print()
    print("-"*51)
    print(f'{"KEY":<6} {"Nama":<20} {"NIM":>12} {"SKS":>3} {"Tanggal Lahir":>10}')

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY: mahasiswa})

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')

        print(f'{KEY:<6} {NAMA:<20} {NIM:>12} {SKS:>3} {LAHIR:>10}')

    break
