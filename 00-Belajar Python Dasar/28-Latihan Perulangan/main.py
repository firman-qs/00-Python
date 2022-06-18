# clear before run 
from dataclasses import dataclass
import os
from re import I
os.system('cls')


#
sisi = 11

# menggambar segitiga siku2 menggunakan while loop
a = 1
b = "|"
while a <= sisi  :
    print(b*a)
    a += 1

print(20*"-"+" bentuk 1 \n")


# menggambar segitiga siku2 menggunakan for loop
for i in range(1,(sisi+1)):
    print("\\"*i)


print(20*"-"+" bentuk 2 \n")

# menggambar segitiga siku2 menggunakan break 
a = 1
while True :
    if a > sisi :
        break
    print("|_"*a)
    a+=1

print(20*"-"+" bentuk 3 \n")

# menggambar segitiga ganjil doang
a = 0
while True :
    a+=1
    if  a > sisi:
        break
    if (a%2) == 0 :
        continue
    print("^"*a)

print(20*"-"+" bentuk 4 \n")

# segitiga sama kaki menggunakan pengaturan .center
a = 0
while True :
    a+=1
    if  a > sisi:
        break
    if (a%2) == 0 :
        continue
    d = ("*"*a).center(sisi)
    print(d)

print(20*"-"+" bentuk 5 \n")

# segitiga sama kaki menggunakan pengaturan spasi
a = 0
while True :
    a+=1
    if  a > sisi:
        break
    if (a%2) == 0 :
        continue
    d = (" "*int((sisi - a)/2) + "*"*a)
    print(d)


""" dapet dari yutup 

print(20*"-"+"sama sisi")
for i in range(0, 5):
    print(" " * (5 - i), end = "")
    for x in range(i):
        print("+ ", end = "")
    print()
for i in range(5, 0, -1):
    print(" "*(5-i), end='')
    for x in range(i):
        print("- ", end='')
    print()
    
"""

print(20*"-"+" bentuk 6 \n")

# belah ketupat menggunakan pengaturan .center
a = 0
if (sisi % 2) == 0 :
    while True :
        a+=1
        if  a > (sisi*2):
            break
        if (a%2) == 0 :
            continue
        if a <= sisi:
            d = ("+"*a).center(sisi)
        if a > sisi:
            d = ("-"*(2*(sisi-1)-a)).center(sisi)
        print(d)
if (sisi % 2) != 0 :
    while True :
        a+=1
        if  a > (sisi*2):
            break
        if (a%2) == 0 :
            continue
        if a <= sisi:
            d = ("+"*a).center(sisi) # menggunakan emoticon
        if a > sisi:
            d = ("="*(2*(sisi)-a)).center(sisi) # menggunakan emoticon
        print(d)

print(20*"-"+" bentuk 7 \n")
