telat_haid = int(input("Berapa minggu anda terlambat haid : "))
usia_kehamilan = int(input("Berapa minggu usia kehamilan anda :  "))
pendarahan = bool(int(input("Apakah Anda mengalami pendarahan? Jika Ya (Ketik 1) atau Tidak (Ketik 0) : ")))
hasil_konsepsi = bool(int(input("Apakah Hasil Konsepsi masih baik dalam kandungan? Jika Ya (Ketik 1) atau Tidak (Ketik 0) : ")))
mulas = bool(int(input("Apakah merasa mulas sedikit? Jika Ya (Ketik 1) atau Tidak (Ketik 0) : ")))
tes_kehamilan = bool(int(input("Apakah Tes Kehamilan/HCG masih Positif? Jika Ya (Ketik 1) atau Tidak (Ketik 0) : ")))
mulut_rahim = bool(int(input("Apakah Mulut Rahim/Cervix masih dalam kondisi menutup? Jika Ya (Ketik 1) atau Tidak (Ketik 0) : ")))
nyeri_perut = bool(int(input("Apakah anda merasa nyeri di perut bagian bawah? Jika Ya (Ketik 1) atau Tidak (Ketik 0) : ")))

print(telat_haid, usia_kehamilan, pendarahan, hasil_konsepsi, mulas, tes_kehamilan, mulut_rahim, nyeri_perut)



if (telat_haid < 20) & (usia_kehamilan < 20) & (pendarahan == True) & (hasil_konsepsi == True) & (mulas == True) & (tes_kehamilan == True) & (mulut_rahim == True) & (nyeri_perut == True):
    print("Anda di diagnosa mengalami sakit Abortus Imminens")
else:
    print("Anda tidak mengalami sakit Abortus Imminens")
