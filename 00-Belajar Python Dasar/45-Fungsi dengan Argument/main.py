# Fungsi dengan Argumen (input)
'''bentuknya -->
def nama_fungsi(argumen/parameter/input):
    badan_fungsi
'''

# Program tampilkan hello
# def hello(nama):
#     print(f'Selamat datang "{nama}"')
#
# nama = input("Nama : ")
# hello(nama)
#
# # Program tambah
# def tambah(angka1,angka2):
#     hasil = angka1 + angka2
#     print(f"Hasil tambah = {hasil}")
#
# angka1 = int(input("Angka 1 = "))
# angka2 = int(input("Angka 2 = "))
# tambah(angka1,angka2)

# say hi!
def say_hi(x):
    data = x.copy()
    for hero in data:
        print(f"Hai {hero}")

heroDota = ["Hoodwink", "Leshraac", "Drow Ranger"]
say_hi(heroDota)

# fungsi kuadrat
def f():
    x_maxx = int(input("Masukkan nilai X maksimum : "))

    print(f"Fungsi Kuadrat")
    print(f"{'x':^5}|{'y':^5}")

    for x in range(x_maxx):
        y = x**2
        print(f"{x:^5}|{y:^5}")
f()


# fungsi kubik
def say_hi(x):
    data = x.copy()
    for hero in data:
        y = hero**3
        print(f"{hero},{y}")

nmax = int(input("Masukkan Nilai X Maksimum : "))
heroDota = [i for i in range(nmax)]
say_hi(heroDota)