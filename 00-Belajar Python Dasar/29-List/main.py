
# clear before run 
from dataclasses import dataclass
import os
from re import I

from numpy import append
os.system('cls')


# --- LIST ---
# kumpulan data 


# kumpulan data number
data_angka = [1,3,6,7,2,3,4,5]
print(f"{data_angka} dengan type: {type(data_angka)}")

# kumpulan data string
data_string = ["arc warden","mars","spectre","A","b"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# kumpulan data campuran(boolean, string, number)
data_campuran = [False, 60, "Juggernaut"]
print(data_campuran)

# membuat list dengan casting range() ke list
data_range = range(0,(20+1),2) # range(start,stop,step)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
data_list_for = [2**i for i in range(0,11)]
print(data_list_for)

# membuat list dengan for loop dan if
data_list_for_if = [i for i in range(0,10+1) if i%2 == 0]
print(data_list_for_if)


# program mencari biner
print("\n"+9*"~"+" Mencari Biner "+9*"~")

des = int(input("Masukkan angka desimal : "))
desbin = [2**i for i in range(9,-1,-1)]
print(desbin)

print(39*"-"+" binernya")

listBin = ["sign"]
for i in range(0,10):
    if desbin[i]>des:
        listBin += [0]
    if desbin[i]<des:
        listBin += [1]
        des = des-desbin[i]
    if desbin[i]==des:
        listBin += [1]
        des = des-desbin[i]

print(listBin)

print("")