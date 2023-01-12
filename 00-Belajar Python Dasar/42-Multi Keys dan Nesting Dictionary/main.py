import datetime as dt

mahasiswa1 = {
    "nama":"Davion Dragon",
    "nim":"210321606892",
    "sks_lulus":41,
    "beasiswa":True,
    "lahir":dt.datetime(2003,10,16)
}

mahasiswa2 = {
    "nama":"Crystal Maiden",
    "nim":"220321606892",
    "sks_lulus":20,
    "beasiswa":False,
    "lahir":dt.datetime(2004,8,16)
}

mahasiswa3 = {
    "nama":"Mirana Moon",
    "nim":"190321606892",
    "sks_lulus":62,
    "beasiswa":True,
    "lahir":dt.datetime(2002,12,2)
}

data_mahasiswa = {
    "MAH001" : mahasiswa1,
    "MAH002" : mahasiswa2,
    "MAH003" : mahasiswa3
}
print(f"{data_mahasiswa['MAH001']['beasiswa']}")



print("="*72)
print("-"*72)
print(f"{'No.':^2}| {'Nama':^17} | {'NIM':^12} | {'SKS':^6} | {'Beasiswa':^6} | {'Lahir':^10} |")

no = 1
for mahasiswa in data_mahasiswa:

    LAHIR = data_mahasiswa[mahasiswa]['lahir'].strftime("%x")

    print(f"{no:^2} | {data_mahasiswa[mahasiswa]['nama']:<17} | {data_mahasiswa[mahasiswa]['nim']:>12} | {data_mahasiswa[mahasiswa]['sks_lulus']:>6} | {data_mahasiswa[mahasiswa]['beasiswa']:^6}   | {LAHIR:>10} |")

    no += 1

print("="*72)