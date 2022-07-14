''' Latihan Fungsi '''
import os

# # program untuk menghitung luas dan keliling persegi panajang

# # Membuat Header Program
# print(f"{''.center(48,'=')}")
# print(f"{' PROGRAM MENGHITUNG LUAS '.center(48)}")
# print(f"{' DAN KELILING PERSEGI PANJANG '.center(48)}")
# print(f"{''.center(48,'=')}")

# # Mengambil user input
# PANJANG = int(input('Masukkan Panjang : '))
# LEBAR = int(input('Masukkan Lebar : '))

# # Program menghitung luas & keliling
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)
# # Tampilkan hasil
# print(f"Luas Persegi Panjang = {LUAS}")
# print(f"Keliling Persegi Panjang = {KELILING}")


def header():
    '''Fungsi Header'''
    os.system('cls')
    print(f"{''.center(48,'=')}")
    print(f"{' 📏 PROGRAM MENGHITUNG LUAS '.center(48)}")
    print(f"{' DAN KELILING PERSEGI PANJANG '.center(48)}")
    print(f"{''.center(48,'=')}")

def inputUser():
    panjang = int(input('Masukkan Panjang : '))
    lebar = int(input('Masukkan Lebar : '))
    return panjang, lebar
    
def hitungLuasKeliling(PANJANG, LEBAR):
    luas = PANJANG*LEBAR
    keliling = 2*(PANJANG+LEBAR)
    return luas, keliling
    
def tampilkanHasil(LUAS, KELILING):
    print(f"Luas Persegi Panjang = {LUAS}")
    print(f"Keliling Persegi Panjang = {KELILING}")

# Main Program
while True:
    header()
    PANJANG, LEBAR = inputUser()
    LUAS, KELILING = hitungLuasKeliling(LEBAR=LEBAR, PANJANG=PANJANG)
    tampilkanHasil(LUAS, KELILING)
    
    isContinue = input('\nApakah lanjut (y/n)? ')
    if isContinue == 'n':
        break

print('Pogram Selesai 😊')