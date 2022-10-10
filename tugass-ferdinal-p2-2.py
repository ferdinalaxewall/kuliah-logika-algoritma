# • Seorang pedagang mangga menjual dagangannyayang setiap kg mangga dihargai dengan harga tertentu. Setiap pembeli membayar harga mangga yang dibeli nya berdasarkan berat.
# • Tentukan algoritma pedagang untuk menentukan harga yang harus dibayar pembeli.

# • Identifikasi masalah

# • Input: harga per kg(hrg), berat pembelian(brt)
# • Output: harga yang dibayar pembeli(byr)

print("Masukkan harga mangga perkilogram (kg)")
hrg = int(input())

print("Harga mangga adalah =", hrg, "/ kg")

print("\nMasukkan jumlah berat mangga yang akan di beli (kg)")
brt = int(input())

byr = hrg*brt
print("Jumlah yang harus dibayar adalah", byr)