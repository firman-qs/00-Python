# 31-Operasi List

number = [1,2,3,4,4,1,1,2,3,1,5,1,2,3,7,8,2,1,0,9]
print(f"number = {number}")

# menghitung/count data
jumlah = number.count(1)
print(f'angka 1 sebanyak = {jumlah}')

# ambil posisi data (index)
string = ["Hoodwink", "Grimstroke", "Mars"]
print(f"data string = {string}")
index = string.index("Mars")
print(f"\"Mars\" berada pada = {index}")

# mengurutkan list (sort)
'''
variablexxxxxx.sort()

atau

variablexxxxxx.sort(reverse=True/False, key=fungsi)
'''
number.sort()
print(f"number sorted = {number}")
string.sort()
print(f"string sorted = {string}")

# reverse urutan data
number.reverse()
print(f"number reverse = {number}")
string.reverse()
print(f"string reverse = {string}")

# urutkan terbalik
number = [1,3,4,2,9,6,7,5,8]
print(f"number awal = {number}")
number.sort(reverse=True)
print(f"number urut terbalik = {number}")

