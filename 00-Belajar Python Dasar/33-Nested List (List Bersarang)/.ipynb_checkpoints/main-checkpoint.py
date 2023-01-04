# Nested List / List Bersarang

dataList_0 = [1,2,3]
dataList_1 = [4,5,6]

dataList_biasa = ["Mars", "Zeus", "Grimstroke"]

print(f"list biasa = {dataList_biasa}")

list_2D = [dataList_0,dataList_1,dataList_biasa] # Nester List

print(f"list bersarang = \n{list_2D}")

# contoh penggunaan 

print("\n" + 8*"~"+ " Data Mahasiswa " +8*"~")
mahasiswa_0 = ["Zeus",25,"Fisika"]
mahasiswa_1 = ["Mars",23,"Biologi"]
mahasiswa_2 = ["Oracle",21,"Kimia"]

list_mahasiswa = [mahasiswa_0,mahasiswa_1,mahasiswa_2]

print(f"mahasiswa = {list_mahasiswa}\n")


for mahasiswa in list_mahasiswa:
    print(f"nama \t: {mahasiswa[0]}")
    print(f"umur \t: {mahasiswa[1]}")
    print(f"jurusan\t: {mahasiswa[2]}\n")


# dengan reference

list_copy = list_mahasiswa.copy();
print(f"mahasiswa = {list_copy}")
mahasiswa_0[0] = "michael"
print(f"mahasiswa = {list_copy}")
print(f"mahasiswa = {list_mahasiswa}")
