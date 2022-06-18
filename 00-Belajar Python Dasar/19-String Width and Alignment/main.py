# -*- coding: utf-8 -*-
"""
Created on Mon May 23 16:01:29 2022

@author: fqs
"""
#? String Width and Alignment

# Data
namaLengkap = "Ammar The Flower"
nomorNIM    = "123454321"
nomorAbsen  = "11"
offering    = "AC"

# syntax standar/biasa
data_string = f"Nama = {namaLengkap}, NIM = {nomorNIM}, Absen = {nomorAbsen}, Offering = {offering}"

bar = " String Standart ".center(30,"=")
print("\n"+bar)
print(data_string)


# multiline string menggunakan \n enter/newline
data_string = f"Nama = {namaLengkap}, \nNIM = {nomorNIM}, \nAbsen = {nomorAbsen}, \nOffering = {offering}"

bar = " String Multiline ".center(30,"=")
print("\n" + bar)
print(data_string)


# multiline string dengan kutip dua 3x triplets
data_string = f"""Nama\t = {namaLengkap} 
NIM\t = {nomorNIM}
Absen\t = {nomorAbsen}
Offering = {offering}"""

bar = " String Multiline ".center(30,"=")
print("\n" + bar)
print(data_string)

# mengatur lebar
data_string = f"""Nama\t = "{namaLengkap:>30}"
NIM\t = "{nomorNIM:>30}"
Absen\t = "{nomorAbsen:>20}"
Offering = "{offering:>10}\""""

bar = " String Multiline ".center(30,"=")
print("\n" + bar)
print(data_string)


