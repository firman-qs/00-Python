"""
# looping dari list
# @author https://github.com/kelasterbuka
"""
# for loop
print("For Loop")
kumpulan_angka = [4, 3, 2, 5, 6, 1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["ucup", "otong", "dadang", "diding", "dudung"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("\nFor Loop dan range")
kumpulan_angka = [10, 5, 4, 2, 6, 5]

PANJANG = len(kumpulan_angka)

for i in range(PANJANG):
    print(f"angka = {kumpulan_angka[i]}")

# while loop
print("\nWhile loop")
kumpulan_angka = [10, 5, 4, 2, 6, 5]

PANJANG = len(kumpulan_angka)
i = 0

while i < PANJANG:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension
print("\nList Comprehension")
data = ["ucup", 1, 2, 3, "otong"]

[print(f"data={i}") for i in data]

angka = [10, 5, 4, 2, 6, 5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\nEnumerate")
data_list = ["ucup", 1, 2, 3, "otong"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")

print("\nnon-Enumerate")

for i in data_list:
    print(f"index = {data_list.index(i)}, data = {i}")
