"""Membaca file eksternal"""
import os
os.system("cls")

print(f"{' Membaca file txt '.center(44,'=')}")

# buka data dengan mode "read" only
file = open("data.txt", mode="r")
print(f"status read: {file.readable()}")
print(f"status write {file.readable()}")

# membaca seluruh file
print(file.read())

# membaca baris per baris
# print(file.readline(), end='')
# print(file.readline(), end='')

# membaca semua baris sebagai list, setiap baris kedalam komponen list
# print(file.readlines())

# close file
print(f"apakah file sudah diclose: {file.closed}")
file.close()
print(f"apakah file sudah diclose: {file.closed}")

# salah satu teknik membaca file di python
print(f"\n{' Membaca file txt dengan with '.center(44,'=')}")
with open("data.txt", mode='r') as file:
    # membaca seluruh file
    content = file.read()
    print(content)
    print(f"apakah file sudah diclose: {file.closed}")
# tidak perlu .close() file
print(f"apakah file sudah diclose: {file.closed}")
