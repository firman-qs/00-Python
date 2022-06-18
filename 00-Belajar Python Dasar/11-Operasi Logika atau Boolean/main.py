
#? Operasi Logika atau Boolean
## not, or, and xor

## not
from re import A


print('====NOT====')
a = False
c = not a
print('data a =', a)
print('--------------NOT')
print('data c =', c)

## or
print('====OR====') #akan true jika salah satu true
a = True
b = True
c = a or b
print(a,'OR',b,'  =',c)
a = True
b = False
c = a or b
print(a,'OR',b,' =',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

## and
print('====AND====') #akan true jika dua-duanya true
a = True
b = True
c = a and b
print(a,'AND',b,'  =',c)
a = True
b = False
c = a and b
print(a,'AND',b,' =',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

## or
print('====XOR====') #akan true jika salah satu true
a = True
b = True
c = a ^ b
print(a,'XOR',b,'  =',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,' =',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)