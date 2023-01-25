"""Docstring"""
import os
os.system("cls")

# fungsi biasa
def fungsi_kuadrat(angka):
    """kembalikan angka kuadrat"""
    return angka**2


print(f"hasil fungsi kuadrat: {fungsi_kuadrat(5)}")

# fungsi lambda
lambda_kuadrat = lambda angka : angka**2

print(f"hasil lambda kuadrat: {lambda_kuadrat(5)}")

## penggunaan
# sorting list biasa (berdasarkan alphabet)
data_list = ["Otong", "Dudung", "Ucup"]
data_list.sort()
print(f"sorted list biasa = {data_list}")

# sorting list dengan lambda (berdasarkan panjang string)
data_list = ["Otong", "Dudung", "Ucup"]
data_list.sort(reverse = False, key = lambda nama : len(nama))
print(f"sorted list lambda = {data_list}")

# Filter
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_angka_ganjil = list(filter(lambda x:x%2!=0, data_angka))
print(f"data angka ganjil = {data_angka_ganjil}")


# Anonymous function
# currying <- Haskell Curry
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"Lima pangkat 2 = {pangkat2(5)}")