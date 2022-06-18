#konversi suhu



print("\n===== PROGRAM KONVERSI SUHU =====\n")  #\n adalah sintax untuk memberikan "enter di-sebelum/sesudah teks"

unit = input("Pilih Skala Suhu Awal (re,fah,cel,kel) : ")

if unit=="cel" :

    c   = float(input("\nMasukkan Suhu dalam Celcius  = "))
    print("Suhu dalam celcius           =", c,"Celcius")

    r = (4/5) * c
    print("Suhu dalam Reamur adalah     =", r, "Reamur")

    f = ((9/5) * c) + 32
    print("Suhu dalam Fahrenheit adalah =", f, "Fahrenheit")

    k = c + 273
    print("Suhu dalam Kelvin adalah     =", k, "Kelvin\n")

elif unit=="re" :

    r   = float(input("\nMasukkan Suhu dalam Reamur   = "))
    print("Suhu dalam Reamur            =", r,"Reamur")

    c = (5/4) * r
    print("Suhu dalam Celcius adalah    =", c, "Celcius")

    f = ((9/4) * r) + 32
    print("Suhu dalam Fahrenheit adalah =", f, "Fahrenheit")

    k = c + 273
    print("Suhu dalam Kelvin adalah     =", k, "Kelvin\n")   


