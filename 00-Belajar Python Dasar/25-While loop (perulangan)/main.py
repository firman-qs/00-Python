# clear before run 
from dataclasses import dataclass
import os
from re import I
os.system('cls')


# While loop perulangan
''' syntax

awal program --> while kondisi(boolean.True):
                    aksi

                akhir program

'''

# bilangan real menggunakan while loop
bar = " Bilangan real ".center(36,"~")
print(bar)

a = 0
while a <= 10 :         #range 0 - 10
    print(f"{a}")
    a = a+1


# bilangan genap menggunakan while loop
bar = " Bilangan genap 1 ".center(36,"~")
print(bar)

a = 2
while a <= 10 :         #range 0 - 10
    print(f"{a}")
    a = a+2             #menggunakan a+2

bar = " Bilangan genap 2 ".center(36,"~")
print(bar)
a = 2
while (a % 2) == 0 and a <= 10 :    #range 0 - 10
    print(f"{a}")
    a = a+2                         #menggunakan a+2


# bilangan ganjil menggunakan while loop
bar = " Bilangan ganjil 1 ".center(36,"~")
print(bar)

a = 1
while a <= 10 :         #range 0 - 10
    print(f"{a}")
    a = a+2             #menggunakan a+2

bar = " Bilangan ganjil 2 ".center(36,"~")
print(bar)
a = 1
while (a % 2) != 0 and a <= 10 :    #range 0 - 10
    print(f"{a}")
    a = a+2                         #menggunakan a+2


# bilangan prima menggunakan while loop
bar = " Bilangan prima ".center(36,"~")
print(bar)

prima = "2 "
a = 3
while a <= 15 :
    status = True
    for x in range(2,a):
        if a%x == 0:
            status = False
    if status==True:
        prima = prima + str(a) + " "
    else: pass
    a += 1
print(prima)