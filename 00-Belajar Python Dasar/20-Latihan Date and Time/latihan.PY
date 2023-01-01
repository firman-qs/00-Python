# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 11:40:15 2022
@author: fqs
"""
# ? latihan date and time
# import module section
import os
import datetime as dt

# clear console first
os.system("cls")

# date and time ==> menghitung umur
print("Silakan masukkan tanggal, bulan, dan tahun lahir")
tanggal = int(input("tanggal\t: "))
bulan = int(input("bulan\t: "))
tahun = int(input("tahun\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
hari_ini = dt.date.today()

print(f"Anda lahir pada {tanggal_lahir:%A}, {tanggal_lahir}")
print(f"Hari ini adalah {hari_ini:%A}, {hari_ini}")

umur_hari = hari_ini-tanggal_lahir
umur_tahun = hari_ini.year - tanggal_lahir.year
umur_bulan = int((umur_hari.days % 365) // 30.4166666667) # 30.4166666667 rata-rata hari dari 12 bulan (jika februari = 28)
umur_hari_lebih = int(((umur_hari.days % 365) % 30.4166666667))
print(
    f"Umur anda adalah {umur_tahun} tahun, {umur_bulan} bulan, {umur_hari_lebih} hari")
