

#? Format String

## Contoh Umum

### String

hello = "Hello World !"
format_string = f"Says: {hello}"
print(format_string)

### Booleang
boolean = True
format_string = f"Boolean: {boolean}"
print(format_string)

### Angka
angka = 1999.3
format_string = f"Angka = {angka}"
print(format_string)


## Bilangan Bulat
tahun = 2005
format_string = f"Tahun: {tahun:d}"
print(format_string)

## Bilangan dengan ordo ribuan
harga = 5670000
format_string = f"Harga: {harga:,}"
print(format_string)

## Bilangan desimal
avogadro = 6.02214076
format_string = f"avogadro: {avogadro:.2f}"
print(format_string)

## Bilangan notasi ilmiah
avogadro = 6.02214076*(10**23)
format_string = f"avogadro: {avogadro:.9E}"
print(format_string)

## menampilkan leading zero
limaDigit = 25
format_string = f"Lima Digit dari {25} adalah {limaDigit:05}"
print(format_string)

## menampilkan tanda + atau -
angkaPlus = 9
angkaMinus = -7
formatPlus = f"Angka Plus = {angkaPlus:+}"
formatMinus = f"Angka Minus = {angkaMinus:+}"
print(formatPlus)
print(formatMinus)

## menformat persentase
persentase = 0.019
format_persen = f"Persentase = {persentase:.2%}"
print(format_persen)

## operasi aritmatika dalam placeholder
nilai1 = 95
nilai2 = 90
nilai3 = 87
format_string = f"Nilai rata-rata = {(nilai1+nilai2+nilai3)/3}"
print(format_string)

## format angka lain (binary, octal, hexadecimal)
desimal = 255
format_string = f'''Angka Desimal = {desimal}
Angka octal = {oct(desimal)}
Angka hex = {hex(desimal)}
'''
print(format_string)
