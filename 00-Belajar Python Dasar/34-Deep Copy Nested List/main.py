from copy import deepcopy as dc

data_asli = [[1,2],[7,8,9],2]
data_copy = data_asli.copy()
data_deep = dc(data_asli)

print(f"{data_asli}, data[0][1] in {hex(id(data_asli[0][1]))}")

print(52*"-"+" menjadi:")

data_asli[0][1] = 3

print(f"{data_asli}, data[0][1] in {hex(id(data_asli[0][1]))}")
print(f"{data_copy}, data[0][1] in {hex(id(data_copy[0][1]))}")
print(f"{data_deep}, data[0][1] in {hex(id(data_deep[0][1]))}")