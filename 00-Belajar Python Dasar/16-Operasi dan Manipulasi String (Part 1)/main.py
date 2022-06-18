
#! Operasi dan Manipulasi String

#* 1. Menyambung string (concatenate) menggunakan tanda (+)

nama_pertama    = "Firman"
nama_tengah     = "Qashdus"
nama_akhir      = "Sabil"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print("\n" + nama_lengkap)

#* 2. Menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

#* 3. Operator untuk string
## Cek apakah ada sebuah komponen char/str pada sebua string
d = "d"
status = d in nama_lengkap
print("Huruf " + '"'+ d +'"' + " ada di dalam " + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print("Huruf " + '"'+ D +'"' + " ada di dalam " + nama_lengkap + " = " + str(status))

D = "D"
status = D not in nama_lengkap
print("Huruf " + '"'+ D +'"' + " ada di dalam " + nama_lengkap + " = " + str(status))

## mengulang string
wk = "wk"
print(wk*3)
print("wk"*10)

## indexing string
print("index ke-0 = "+ nama_lengkap[0]) # dimulai dari 0
print("index ke-1 = "+ nama_lengkap[1]) # index bebas
print("index ke-6 = "+ nama_lengkap[6]) # index bebas
print("index ke-(-1) = "+ nama_lengkap[-1]) # indexing dari dibelakang
print("index ke-(-2) = "+ nama_lengkap[-2]) # indexing dari dibelakang
print("index ke-(0,5) = "+ nama_lengkap[0:6]) # dimulai dari index 0 sampai sebelum 5
print("index ke-(7,13) = "+ nama_lengkap[7:14]) # dimulai dari index 7 sampai sebelum 14
print("index ke-[0,2,4,6,8] : " + nama_lengkap[0:21:2]) # diambil index 0,2,4,6,8

## item paling kecil
a = nama_lengkap
print("nilai terkecil dari : " + a + " = " + min(str(id(a))))
print("nilai terbesar dari : " + a + " = " + max(str(id(a))))

### string ditulis dalam kode ASCII
ascii_code = ord(" ")
print('ASCII code dari "spasi" adalah : ' + str(ascii_code))
ascii_code = ord("u")
print('ASCII code dari "u" adalah : ' + str(ascii_code))

dataASCII = 117
print("character dari ASCII code 117 adalah : " + chr(dataASCII))

## 4. Operator dalam bentuk method
data = "0t0ng sur0t0ng parar0t0ng"
jumlah = data.count("0")
print("jumlah o di " + data + " : " + str(jumlah))

b = nama_lengkap + nama_akhir
print(b)


print("\n========= SIID_UM =========")
nama = input("Masukkan Nama anda : ")
nim = input("Masukkan Nim anda  : ")

tahun = nim[0:2]
if tahun=="21" : angkatan = "2021"
elif tahun=="20" : angkatan = "2020"
elif tahun=="19" : angkatan = "2019"
elif tahun=="18" : angkatan = "2018"

faculty = nim[2:4]
if faculty=="03" : fakultas = "Matematika dan Ilmu Pengetahuan Alam"
elif faculty=="02" : fakultas = "Sastra"
elif faculty=="01" : fakultas = "Ilmu Pendidikan"
elif faculty=="04" : fakultas = "Ekonomi"
elif faculty=="05" : fakultas = "Teknik"
elif faculty=="06" : fakultas = "Ilmu Keolahragaan"
elif faculty=="07" : fakultas = "Ilmu Sosial"
elif faculty=="08" : fakultas = "Pendidikan Psikologi"

study = nim[4:6]
if study=="11" : prodi = "S1 Pendidikan Matematika - PMat"
elif study=="12" : prodi = "S1 Matematika - Mat"
elif study=="21" : prodi = "S1 Pendidikan Fisika - PFis"
elif study=="22" : prodi = "S1 Fisika - Fis"
elif study=="31" : prodi = "S1 Pendidikan Kimia*) - PKim"
elif study=="32" : prodi = "S1 Kimia*) - Kim"
elif study=="41" : prodi = "S1 Pendidikan Biologi*) - PBio"
elif study=="42" : prodi = "S1 Biologi*) - Bio"
elif study=="43" : prodi = "SS1 Biteknologi*) - Bio"
elif study=="51" : prodi = "S1 Pendidikan Ilmu Pengetahuan Alam*) - PIPA"


print("\n========= Output =========")
print(
'''Nama \t\t: '''+ nama + '''
NIM \t\t: ''' +nim+ '''
Fakultas \t: ''' +fakultas+ '''
Prodi \t\t: ''' +prodi+ '''
Angkatan \t: '''+angkatan
)




































print("")
































print(" ")
