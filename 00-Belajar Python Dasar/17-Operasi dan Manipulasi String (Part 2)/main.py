#? Operator dalam bentuk methods

## merubah case pada string
bar = " PART 17 ".center(40,"-")
print(bar)

## UPPERCASE
bar = " UPPERCASE ".center(40,"=")
print("\n" + bar)
nama = "Firman Qashdus Sabil"
print("normal = " + nama)
nama = nama.upper()
print("upper = " + nama)

### lowercase
bar = " lowercase ".center(40,"=")
print("\n" + bar)
alay = "nGaKAk AbiEzzZZz"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX methodg

## contoh pengecekan lowercase
bar = " islower ".center(40,"=")
print("\n" + bar)
salam = "assalamualaikum"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))
bar = " isupper ".center(40,"=")
print("\n" + bar)
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <- untuk mengecek apakah huruf semua
bar = " isalpha ".center(40,"=")
print("\n" + bar)
alphabet = "WellPlayed"
alphabetWithSpace = "Well Played"
alphaAndNum = "W33"
apakah1_alpha = alphabet.isalpha()
apakah2_alpha = alphaAndNum.isalpha()
apakah3_alpha = alphabetWithSpace.isalpha()
print(str(alphabetWithSpace) + " isAlpha = " + str(apakah3_alpha) + ",\n" + str(alphabet) + " isAlpha = " + str(apakah1_alpha) + ", dan\n" + str(alphaAndNum) + " isAlpha = " + str(apakah2_alpha))

# isalnum() <- apakah huruf dan angka
bar = " isalnum ".center(40,"=")
print("\n" + bar)
alphabet = "WellPlayed"
alphabetWithSpace = "Well Played"
alphaAndNum = "W33"
apakah1_alpha = alphabet.isalnum()
apakah2_alpha = alphaAndNum.isalnum()
apakah3_alpha = alphabetWithSpace.isalnum()
print(str(alphabetWithSpace) + " isAlNum = " + str(apakah3_alpha) + ",\n" + str(alphabet) + " isAlNum = " + str(apakah1_alpha) + ", dan\n" + str(alphaAndNum) + " isAlNum = " + str(apakah2_alpha))

# isdecimal() <- apakah numeric
# isspace() <- apakah isinya spasi, tab dan enter (newline \n)
# istitle() <- huruf pertama setiap kata upper case (Capitalize Each word)


# startwith() dan endwith() <-- keren
bar = " Start & End with ".center(40,"=")
print("\n" + bar)
nama = "Firman Qashdus Sabil"
cek_start = nama.startswith("Firman")
print(str(nama) + " diawali dengan" + "Firman = " + str(cek_start))
cek_ends = "Firman Qashdus Sabil".endswith("Sabil")
print(str(nama) + " diakhiri dengan" + "Firman = " + str(cek_ends))

# join() dan split() <-- buat orang males
bar = " join and split ".center(40,"=")
print("\n" + bar)
pisah = ['aku','sayang','kamu']
gabungan = ' ehm '.join(pisah)
print(pisah)
print(gabungan)

gabungan = "naik vespa keliling kota"
pisah = gabungan.split()
print(gabungan)
print(pisah)

gabungan = "naikehmvespaehmkelilingehmkota"
pisah = gabungan.split("ehm")
print(gabungan)
print(pisah)

pisah = ["1","2"] #mirip array
gabungan = ' ehm '.join(pisah)
print(pisah)
print(gabungan)


# alokasi karakter
bar = " charracter allocation ".center(40,"=")
print("\n" + bar)
print("'kiri      '")

kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
print("'" + kanan + "'")

kiri = "kiri".ljust(20) # rata kiri dengan 20 karakter
print("'" + kiri + "'")

tengah ="tengah".center(20) # rata tengah dengan 20 karakter
print("'" + tengah + "'")

tengah ="tengah".center(20,'-') # rata tengah dengan 20 karakter
print("'" + tengah + "'")

# kebalikan dari alokasi karakter
bar = " character strip/reverse ".center(40,"=")
print("\n" + bar)
kanan = kanan.strip()
print("'" + kanan + "'")
tengah = tengah.strip('-')
print("'" + tengah + "'")




print()











