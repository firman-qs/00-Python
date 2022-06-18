
#? Operasi Aritmatika

'''
Prioritas Operasi /  Operational precedence
    1. whatever in bracket ()
    2. opartion of: * / % // **
    3. opartion of: + and -
'''

a = 10
b = 3
print("             ")
## Penjumlahan +
hasil = a + b
print(a,"+",b,'=',hasil)

## Pengurangan -
hasil = a - b
print(a,"-",b,'=',hasil)

## Perkalian *
hasil = a * b
print(a,"*",b,'=',hasil)

## Pembagian / 
hasil = a / b
print(a,"/",b,'=',hasil)

## Pangkat (eksponen) **
hasil = a ** b
print(a,"**",b,'=',hasil)

## modulus (sisa bagi)
hasil = a % b
print(a,"%",b,'=',hasil)

## Floor Division //
hasil = a // b
print(a,"//",b,'=',hasil) 

# Prioritas Operasi, Operational Precedence
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//dc',x,"=",hasil) 

print("             ")

print("===MATH OPERATIONAL CHALLENGGE===")
Num1    = int(input("Masukkan angka pertama :"))
op      = input("Masukkan operator :")
Num2    = int(input("Masukkan angka kedua :"))
des     = "Hasilnya adalah ="


if   op=="+"  : 
    hasil=Num1+Num2, type(hasil)
elif op=="-"  : 
    hasil=Num1-Num2, type(hasil)
elif op=="*"  : 
    hasil=Num1*Num2, type(hasil)
elif op=="**" : 
    hasil=Num1**Num2, type(hasil)
elif op=="/"  : 
    hasil=Num1/Num2, type(hasil)
elif op=="%"  : 
    hasil=Num1%Num2, type(hasil)
elif op=="//" : 
    hasil=Num1//Num2, type(hasil)

print(des, hasil)






