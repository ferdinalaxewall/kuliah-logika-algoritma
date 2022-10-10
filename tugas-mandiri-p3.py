# Aldi mempunyai kelereng 15 lebih banyak dari Budi,
# sedangkan Anto mempunyai kelerang 2X jumlah
# kelereng Aldi dan Budi. Agung memiliki kelerang 5
# buah lebih sedikit dari jumlah kelereng Aldi, Budi dan
# Anto. Berapakah jumlah kelereng Budi, Anto dan
# Agung apabila jumlah kelereng Aldi diketahui

def getMaxNumber():

    aldi = int(input("Masukkan Jumlah Kelereng Aldi : "))

    if(aldi >= 15):

        budi = aldi - 15;
        anto = 2 * (aldi + budi)
        agung = (aldi + budi + anto) - 5

        print("Jumlah Kelereng aldi : ", aldi)
        print("Jumlah Kelereng budi : ", budi)
        print("Jumlah Kelereng anto : ", anto)
        print("Jumlah Kelereng agung : ", agung)
    else:
        print("Masukkan angka minimal 15")
        getMaxNumber()

getMaxNumber()