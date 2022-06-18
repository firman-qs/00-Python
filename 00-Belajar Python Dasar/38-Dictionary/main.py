# List --> diakses menggunakan index [i]
# contoh
data_list = ["Abadon","Alchemist","Grimstroke"]
print(data_list[2]) # menggunakan index --> [2]


# Dictionary --> struktur = key:value, diakses dengan key
''' struktur

data_dictionary = {
    key1 : value1,
    key2 : value2,
    key3 : value3
}

'''
# contoh
data_kelas = {
    "mahasiswa" : {
        1 : "Anti mage",
        2 : "Arc Warden",
        3 : "Alchemist"
    },
    "Kelas"     : "AC",
    "Ankatan"   : "2022",
    "list"      : data_list
}

print(data_kelas["mahasiswa"][1]) # menggunakan key --> "mahasiswa"
print(data_kelas["Kelas"]) # menggunakan key --> "mahasiswa"