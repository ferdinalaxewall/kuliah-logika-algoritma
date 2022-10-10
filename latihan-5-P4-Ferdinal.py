## Keterangan
    # gp = Gaji Pokok
    # tjg = Tunjangan
    # lm = Lembur
    # jk = Jam Kerja

gp = int(input("Masukkan Jumlah Gaji Pokok : "))
jk = int(input("Masukkan Jumlah Jam Kerja : "))
tjg = int((20 / 100) * gp)
gaji = gp + tjg
lm = 0

if (jk > 200):
    lm = int((jk - 200) * 20000)

gaji = gp + tjg + lm
pjk = int((10 / 100) * gaji)
gaji_bersih = gaji - pjk

print(f"Gaji Bersih yang pegawai dapatkan adalah Rp. {gaji_bersih}")
print(f"Dengan Rincian : \n\t Gaji Pokok : Rp. {gp} \n\t Tunjangan : Rp. {tjg} \n\t Uang Lembur Rp. {lm} \n\t Total Pendapatan : Rp. {gaji} \n\t Pajak : Rp. {pjk} \n\t Gaji Bersih (Pendapatan - Pajak) : Rp. {gaji_bersih}")