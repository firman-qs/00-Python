def tambah(*args):
    hasil = 0
    for angka in args:
        hasil += angka
    return hasil

def pangkat(n):
    return lambda angka:angka**n