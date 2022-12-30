"""
docstring
"""
#? CASTING  ==> Merubah suatu tipe data kedalam tipe yang lain
# tipe data: float, int, str, bool

## INTEGER
print("====INTEGER====")
data_int = 10
print("Data =", data_int, "type =", type(data_int))
print('konversi>>')
data_float  = float(data_int)
data_str    = str(data_int)
data_bool   = bool(data_int) #boolean false jika nilainya 0
print("Data =", data_float, "type =", type(data_float))
print("Data =", data_str, "type =", type(data_str))
print("Data =", data_bool, "type =", type(data_bool))

# ## FLOAT
print("====FLOAT====")
data_float = 11.2
print("Data =", data_float, "type =", type(data_float))
print('konversi>>')
data_int    = int(data_float) # membulatkan kebawah
data_str    = str(data_float)
data_bool   = bool(data_float) # boolean false jika nilainya 0
print("Data =", data_int, "type =", type(data_int))
print("Data =", data_str, "type =", type(data_str))
print("Data =", data_bool, "type =", type(data_bool))

## STRING
print("====STRING====")
data_str = "10"
print("Data =", data_str, "type =", type(data_str))
print('konversi>>')
data_int    = int(data_str)   # hanya bisa hanya jika angka 
data_float  = float(data_str) # hanya bisa hanya jika angka
data_bool   = bool(data_str)  #
print("Data =", data_int, "type =", type(data_int))
print("Data =", data_float, "type =", type(data_float))
print("Data =", data_bool, "type =", type(data_bool))

## BOOLEAN
print("====BOOLEAN====")
data_bool = False
print("Data =", data_bool, "type =", type(data_bool))
print('konversi>>')
data_str    = str(data_bool)    # hasilnya "False" atau "True"
data_int    = int(data_bool)    # False ==> 0 dan True ==> 1
data_float  = float(data_bool)  # False ==> 0.0 dan True ==> 1.0
print("Data =", data_str, "type =", type(data_str))
print("Data =", data_int, "type =", type(data_int))
print("Data =", data_float, "type =", type(data_float))


