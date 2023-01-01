# clear before run code
from dataclasses import dataclass
import os
os.system('cls')

#? Latihan Date and Time

import datetime as dt

bar = " Program Tanggal Lahir ".center(40,"~")
print("\n"+bar)

#main
print(f"""Masukkan Tangga, Bulan, 
dan Tahun Lahir anda""")
tanggal = int(input("tanggal : "))
bulan   = int(input("bulan \t: "))
tahun   = int(input("tahun \t: "))

tanggalBorn = dt.date(tahun,bulan,tanggal)
print(f"Anda Lahir pada: {tanggalBorn:%A}, {tanggalBorn}")

tanggalNow = dt.date.today()
print(f"Hari ini adalah: {tanggalNow:%A}, {tanggalNow}")

umurHari    = tanggalNow - tanggalBorn
if tanggalNow.month < tanggalBorn.month :
    umurTahun   = (tanggalNow.year - 1) - tanggalBorn.year
    sisaBulan   = tanggalBorn.month - tanggalNow.month
    if tanggalNow.day < tanggalBorn.day:
        sisaHari = tanggalBorn.day - tanggalNow.day
        print(f"Umur anda adalah: {umurTahun} tahun, kurang {sisaBulan} bulan, kurang {sisaHari} hari")
    elif tanggalNow.day > tanggalBorn.day:
        sisaHari = tanggalNow.day - tanggalBorn.day
        print(f"Umur anda adalah: {umurTahun} tahun, kurang {sisaBulan} bulan, lebih {sisaHari} hari")
    elif tanggalNow.day == tanggalBorn.day:
        sisaHari = 0
        print(f"Umur anda adalah: {umurTahun} tahun, kurang {sisaBulan} bulan, {sisaHari} hari")

elif tanggalNow.month > tanggalBorn.month :
    umurTahun   = tanggalNow.year - tanggalBorn.year
    sisaBulan   = tanggalNow.month - tanggalBorn.month
    if tanggalNow.day < tanggalBorn.day:
        sisaHari = tanggalBorn.day - tanggalNow.day
        print(f"Umur anda adalah: {umurTahun} tahun, lebih {sisaBulan} bulan, kurang {sisaHari} hari")
    elif tanggalNow.day > tanggalBorn.day:
        sisaHari = tanggalNow.day - tanggalBorn.day
        print(f"Umur anda adalah: {umurTahun} tahun, lebih {sisaBulan} bulan, lebih {sisaHari} hari")
    elif tanggalNow.day == tanggalBorn.day:
        sisaHari = 0
        print(f"Umur anda adalah: {umurTahun} tahun, lebih {sisaBulan} bulan, {sisaHari} hari")        
    
elif tanggalNow.month == tanggalBorn.month :
    umurTahun   = tanggalNow.year - tanggalBorn.year
    sisaBulan   = 0
    if tanggalNow.day < tanggalBorn.day:
        sisaHari = tanggalBorn.day - tanggalNow.day
        print(f"Umur anda adalah: {umurTahun} tahun, {sisaBulan} bulan, kurang {sisaHari} hari")
    elif tanggalNow.day > tanggalBorn.day:
        sisaHari = tanggalNow.day - tanggalBorn.day
        print(f"Umur anda adalah: {umurTahun} tahun, {sisaBulan} bulan, lebih {sisaHari} hari")
    elif tanggalNow.day == tanggalBorn.day:
        sisaHari = 0
        print(f"Umur anda adalah: {umurTahun} tahun, {sisaBulan} bulan, {sisaHari} hari")   


bar = " import class ".center(40,"~")
print("\n"+bar)
# import class date
from datetime import date
date = date.today()
print(date)



bar = " timedelta selisih waktu ".center(40,"~")
print("\n"+bar)

from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)

print()
