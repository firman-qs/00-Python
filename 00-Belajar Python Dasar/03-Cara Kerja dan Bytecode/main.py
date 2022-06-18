# PROSEDUR KERJA PYTHON :
# Prosedur 1 (interpreter)
# 1. membaca perbaris dari source code xx.py
# 2. interpreter oleh python x.xx
# 3. terminal
# Prosedur 2 (Compile)
# 1. membaca keseluruhan xx.pyc
# 2. compile 
# 3. executable program .pyc
# *cara compile => python -m py_compile xx.py

# *program yang tercompile dijalankan jauh lebih cepat

from pydoc import doc

print ('Helo Dunia')
print ("Hello")
print ("World")
# *baris kosong diabaikan (tdk berpengaruh)

print ('Baris ke 4')

x = range(0, 3)
for i in x: print ('hello world!@!#')

# *urutan penulisan berpengaruh
# contoh jika syntax dibawah diubah posisi satu sama lain
a = 50
print(a)

