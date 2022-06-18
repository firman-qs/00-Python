# Operator Dictionary

data_dict = {
    "np" : "Natures Prophet",
    "am" : "Anti Mage",
    "pa" : "Phantom Assassin"
}

## Panjang Dictionary
lendict = len(data_dict)
print(f"panjang dictionary = {lendict}")

## mengecek key pada dictionary exist atau tidak
key = "np"
checkkey = key in data_dict
print(f'Apakah "{key}" ada di data_dict = {checkkey}')

## mengakses value (read) dengan get()
print(data_dict["np"])
print(data_dict.get("np"))
key = "es"
print(data_dict.get(key,f"data {key} tidak ditemukan"))

## mengupdate data
data_dict["es"] = "Earthshaker" # data baru
print(data_dict)
data_dict["np"] = "Night Prophet" # ubah data lama
print(data_dict)

data_dict.update({"np":"Nature Prophet"})
print(data_dict)
data_dict.update({"ck":"chaos knight"})
print(data_dict)

# men delete data pada dicitonary
del data_dict["ck"]
print(data_dict)







