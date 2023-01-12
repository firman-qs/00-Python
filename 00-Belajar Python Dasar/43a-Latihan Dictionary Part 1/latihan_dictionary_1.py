""" Latihan Dictionary Part a"""
import datetime as dtm
import os

# template dictionary mahasiswa
mahasiswa_template = {
    "nama": "nama",
    "nim": "00000000",
    "sks_lulus": 0,
    "lahir": dtm.date(1111, 11, 1)
}

data_mahasiswa = {}

os.system("cls")
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print(20*"-")

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
mahasiswa["nama"] = input("Nama Mahasiswa: ")
mahasiswa["nim"] = input("NIM Mahasiswa: ")
mahasiswa["sks_lulus"] = input("SKS Lulus: ")
TAHUN = int(input("Tahun Lahir: "))
BULAN = int(input("Bulang Lahir: "))
HARI = int(input("Hari Lahir: "))
mahasiswa["lahir"] = dtm.date(TAHUN, BULAN, HARI)

print(mahasiswa)
