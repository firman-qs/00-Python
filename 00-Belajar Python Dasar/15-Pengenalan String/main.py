
data = "ini adalah string"
print(data)
print(type(data))

#? 1. Cara membuat string
'''
    1. Menggunakan Single Quote '....'
    2. menggunakan Double Quote "...."
'''
data = 'ini menggunakan single quote'
print(data)

data = "ini menggunakan Double quote"
print(data)

print('"Hallo, Apa Kabar?"')
print("'Hallo, Apa Kabar?'")
print("Hari ini adalah hari jum'at")

#? 2. menggunakan tanda backslash \

# membuat tanda ' menjadi string. menggunakan \'
print('Mari shalat jum\'at')

# membuat tanda \ menjadi string. menggunakan \\
print("folrder windows berada di C:\\user\web")

# membuat Tab=> menggunakan \t
print("Nama \t\t: Firman Qashdus Sabil")
print("NIM \t\t: 210321606892")
print("Offering \t: AB")

# backspace (hilangkan spasi) menggunakan \b
print("Ucup \bOtong, Deketan")

# newline. menggunakan \n, \r, \r\n
print("Baris pertama.\nBaris kedua") # LF = line feed -> unix, macOS, linux
print("Baris pertama.\rBaris kedua") # CR = carriage return -> commodore, acorn, lisp
print("Baris pertama.\r\nBaris kedua") # CRLF = line feed carriage return -> Windows


#? 3. String literal atau raw

# !hati-hati
print("lokasi foldernya di E:\new folder")

# menggunakan raw string
print(r"lokasi foldernya di E:\new folder. \n\b\t\r\\\'")

# multiline literal string
print('''
Nama \t\t: Firman Qashdus Sabil
NIM \t\t: 210321606892 
Offering \t: AB''') 

# multiline literal string dan raw
print(r'''
Nama \t\t: Firman Qashdus Sabil
NIM \t\t: 210321606892 
Offering \t: Semester 2\AB
''')


