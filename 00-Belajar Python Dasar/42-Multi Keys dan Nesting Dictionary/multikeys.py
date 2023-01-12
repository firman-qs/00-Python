"""Docstring"""
import datetime as dt
import os
os.system("cls")

mahasiswa_1 = {
    "nama": "Shadow Fiend",
    "nim": "21038921",
    "sks_lulus": 96,
    "beasiswa": True,
    "lahir": dt.datetime(2003, 12, 18)
}

mahasiswa_2 = {
    "nama": "Nature Prophet",
    "nim": "19029393",
    "sks_lulus": 130,
    "beasiswa": False,
    "lahir": dt.datetime(2000, 11, 2)
}

mahasiswa_3 = {
    "nama": "Ember Spirit",
    "nim": "22040156",
    "sks_lulus": 23,
    "beasiswa": True,
    "lahir": dt.datetime(2004, 2, 29)
}

data_mahasiswa = {
    "MAH001": mahasiswa_1,
    "MAH002": mahasiswa_2,
    "MAH003": mahasiswa_3
}

print('-'*63)
print(f"{'KEY':<8} {'Nama':<16} {'NIM':<10} {'SKS':>4} {'Beasiswa':<10} {'Lahir':<10}")
print('-'*63)
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:<8} {NAMA:<16} {NIM:<10} {SKS:>4} {BEASISWA:<10} {LAHIR:<10}")


print()