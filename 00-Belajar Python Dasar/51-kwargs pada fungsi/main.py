# from ast import arg
import os
os.system('cls')

# **kwargs pada fungsi

# def fungsi(nama, tinggi, berat):
#     '''regular function'''
#     print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

# fungsi('pudge',110,100)


def fungsi(**kwargs):
    '''regular function'''
    print(
        f"{kwargs['nama']} punya tinggi {kwargs['tinggi']} dan berat {kwargs['berat']}")


fungsi(nama="pudge", tinggi=110, berat=100)


# contoh
def math(*args, tes, **kwargs):
    print(args)
    print(tes)
    if kwargs['operasi'] == 'tambah':
        print("Operasi Penjumlahan")
        hasil = 0
        for number in args:
            hasil += number
            print(number)
        print(hasil)

    elif kwargs['operasi'] == 'kali':
        print("Operasi Perkalian")
        hasil = args[0]
        for number in args[1:]:
            hasil *= number
        print(hasil)


math(2, 2, 3, tes=2, operasi='tambah')
