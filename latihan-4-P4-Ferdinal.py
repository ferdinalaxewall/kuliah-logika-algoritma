
def minimumPenjualan():
    gaji_pokok = 5000000
    jumlah_produk = int(input("Masukkan Jumlah Produk Terjual : "))

    if (jumlah_produk > 0):
        harga_produk = int(input("Masukkan Harga Produk : "))
        omset = jumlah_produk * harga_produk

        print(f"Gaji Pokok anda Sebesar Rp. {gaji_pokok}")
        print(f"Omset Penjualan anda Sebesar Rp. {omset}")

        if (jumlah_produk > 100):
            print(f"Anda berhak mendapat 20% dari omset penjualan anda, Total Bonus anda Rp. {int(omset * (20 / 100))}")
        else:
            print(f"Anda berhak mendapat 10% dari omset penjualan anda, Total Bonus anda Rp. {int(omset * (10 / 100))}")
    else:
        print("Jumlah Produk yang Terjual minimal 1")
        minimumPenjualan()

minimumPenjualan()