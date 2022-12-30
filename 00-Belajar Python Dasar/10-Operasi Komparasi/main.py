
#? Operasi Komparasi
## setiap hasil dari operasi komparasi adalah boolean
## komparai ==> ==, >, <, >=, <=, !=, is, is not

a=4
b=2

print('\n===== KURANG dan LEBIH DARI (< dan >) =====')
hasil = a > 3
print(a,'>','3','=', hasil)
hasil = b < 3
print(b,'<','3','=', hasil)
hasil = a < 3
print(a,'<','3','=', hasil)
hasil = b < 2
print(b,'<','2','=', hasil)

print('\n===== KURANG dan LEBIH DARI SAMA DENGAN (<=) =====')
hasil = a >= 3
print(a,'>=','3','=', hasil)
hasil = b >= 3
print(b,'>=','3','=', hasil)
hasil = a <= 4
print(a,'<=','3','=', hasil)
hasil = b <= 2
print(b,'<=','2','=', hasil)

print('\n===== SAMA DENGAN (==) =====')
hasil = a==b
print(a,'==','b','=', hasil)
hasil = a==4
print(a,'==','4','=', hasil)
hasil = a==3
print(a,'==','3','=', hasil)


print('\n===== TIDAK SAMA DENGAN (!=) =====')
print(a,b)
hasil = a!=b
print(a,'!=','b','=', hasil)
hasil = a!=4
print(a,'!=','4','=', hasil)
hasil = a!=3
print(a,'!=','3','=', hasil)

print('\n===== komparasi objek identity/id (is, is not)) =====')
x = 5 #assignment membuat objek
y = 5
print('nilai x =', x,'dengan id =',id(x),'atau', hex(id(x)))
print('nilai y =', y,'dengan id =',id(y),'atau', hex(id(y)))
print('x =', x)
print('y =', y)
hasil = x is y
print('x is y =', hasil)
print('===============')
x = 5 #assignment membuat objek
y = 6
print('nilai x =', x,'dengan id =',id(x),'atau', hex(id(x)))
print('nilai y =', y,'dengan id =',id(y),'atau', hex(id(y)))
print('x =', x)
print('y =', y)
hasil = x is not y
print('x is not y =', hasil)

print({format(10, '012b')})