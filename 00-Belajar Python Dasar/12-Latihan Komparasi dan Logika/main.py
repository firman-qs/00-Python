
#? Latihan Komparasi dan Logika
## membuat gabungan area rentang dari angka

## +++++3-----10+++++
print('\n===={ x<3 or x>10 }====')
inputUser = float(input("Masukkan angka yang lebih besar dari 10\n" "atau kurang dari 3 :"))
### cek kurang dari tiga
lessThan3 = inputUser < 3
print('Angka lebih dari 3 =', lessThan3)
moreThan10 = inputUser > 10
print('Angka lebih dari 10 =', moreThan10)
### Hasil input adalah:
inputCorrect = lessThan3 or moreThan10
print('Angka yang anda masukkan :', inputCorrect)


## -----3+++++10-----
print('\n===={ 3<x<10 }====')
inputUser = float(input("Masukkan angka yang lebih besar dari 3\n" "dan kurang dari 10 :"))
### cek kurang dari tiga
moreThan3 = inputUser > 3
print('Angka lebih dari 3 =', lessThan3)
lessThan10 = inputUser < 10
print('Angka kurang dari 10 =', moreThan10)
### Hasil input adalah:
inputCorrect = moreThan3 and lessThan10
print('Angka yang anda masukkan :', inputCorrect)


## -----0+++++5-----8+++++11-----
print('\n===={ 0<x<5 or 8<x<11 }====')
inputUser = float(input("Masukkan angka diantara 0-5 atau 8-11 :"))
between0_5 = 3<inputUser<5
print("Angka antara 0-5 =", between0_5)
between8_11 = 8<inputUser<11
print("Angka antara 8-11 =", between8_11)
### hasil input adalah:
inputCorrect = between0_5 or between8_11
print("Angka yang anda masukkan adalah", inputCorrect)


## +++++0-----5+++++8-----11+++++
print('\n===={ x<0 or 5<x<8 or x>11 }====')
inputUser = float(input("Masukkan angka kurang dari 0 atau antara 5-8 atau lebih dari 11 :"))
lessThan0 = inputUser < 0
print("Angka kurang dari nol =", lessThan0) 
between5_8 = 5<inputUser<8
print("Angka antara 5-8 =", between5_8)
moreThan11 = inputUser > 11
print("Angka lebih dari 11 =", moreThan11)
### hasil input adalah:
inputCorrect = lessThan0 or between5_8 or moreThan11
print("Angka yang anda masukkan adalah", inputCorrect)









print(' ')

