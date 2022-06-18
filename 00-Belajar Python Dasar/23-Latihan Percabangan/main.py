#? Latihan percabangan

bar     = " Kalkulator Sederhana ".center(36,"~")
print(bar)

Num1    = int(input("Masukkan angka pertama : "))
op      = input("Masukkan operator :")
Num2    = int(input("Masukkan angka kedua : "))

if   op=="+"  : 
    hasil=Num1+Num2
    print(f"Hasilnya adalah {hasil}")
elif op=="-"  : 
    hasil=Num1-Num2
    print(f"Hasilnya adalah {hasil}")
elif op=="*"  : 
    hasil=Num1*Num2
    print(f"Hasilnya adalah {hasil}")
elif op=="**" : 
    hasil=Num1**Num2
    print(f"Hasilnya adalah {hasil}")
elif op=="/"  : 
    hasil=Num1/Num2
    print(f"Hasilnya adalah {hasil}")
elif op=="%"  : 
    hasil=Num1%Num2
    print(f"Hasilnya adalah {hasil}")
elif op=="//" : 
    hasil=Num1//Num2
    print(f"Hasilnya adalah {hasil}")
else : print("masukan yang bener dong!, aku pusying")

