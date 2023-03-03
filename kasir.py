import sys
total = []
porsi = []
mkn = []
gelas = []
mnm = []

baris = ("======================================================")
print(baris)
print("-------------- welcome to Angeom store ---------------")
print(baris)
print("ada discount 5% jika anda berbelanja\ndengan harga Rp.50.000 atau selebihnya")
print("______________________________________________________")
print("masukan nama min 4 max 6 huruf")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli         :", pembeli) 

def menu_makanan():
   global porsi
   global total
   global totalmkn
   global mkn
   print("================= Daftar Menu makanan ================")
   print("\t |  1. mie ayam      = Rp.15.000 \t|")
   print("\t |  2. mie ayam baso = Rp.20.000 \t|")
   print("\t |  3. baso biasa    = Rp.15.000 \t|")
   print("\t |  4. baso rudal    = Rp.20.000 \t|")
   print("\t |  5. baso gaji     = Rp.20.000 \t|")
   print("\t |  6. baso beranak  = Rp.25.000 \t|")
   print(baris)
   menu = int(input("Masukkan nomer menu pilihan anda  : "))
   
   if menu == 1:
        jumlah = int(input("Masukkan jumlah porsi : "))
        porsi.append(jumlah)
        totalmkn = 15000 * jumlah
        total.append(totalmkn)
        makan=("mie ayam")
        mkn.append(makan)
        print("harga makanan Rp.",totalmkn)
        tanya()
   elif menu == 2:
        jumlah = int(input("Masukkan jumlah porsi : "))
        porsi.append(jumlah)
        totalmkn = 20000 * jumlah
        total.append(totalmkn)
        makan=("mie ayam baso")
        mkn.append(makan)
        print("harga makanan Rp.",totalmkn)
        tanya()
   elif menu == 3:
        jumlah = int(input("Masukkan jumlah porsi : "))
        porsi.append(jumlah)
        totalmkn = 15000 * jumlah 
        total.append(totalmkn)
        makan=("baso biasa")
        mkn.append(makan)
        print("harga makanan Rp.",totalmkn)
        tanya()
   elif menu == 4:
        jumlah = int(input("Masukkan jumlah porsi : "))
        porsi.append(jumlah)
        totalmkn = 20000 * jumlah
        total.append(totalmkn)
        makan=("baso rudal")
        mkn.append(makan)
        print("harga makanan Rp.",totalmkn)
        tanya()
   elif menu == 5:
        jumlah = int(input("Masukkan jumlah porsi : "))
        porsi.append(jumlah)
        totalmkn = 20000 * jumlah   
        total.append(totalmkn)
        makan=("baso gaji")
        mkn.append(makan)        
        print("harga makanan Rp.",totalmkn)
        tanya()
   elif menu == 6:
        jumlah = int(input("Masukkan jumlah porsi : "))
        porsi.append(jumlah)
        totalmkn = 25000 * jumlah   
        total.append(totalmkn)        
        makan=("baso beranak") 
        mkn.append(makan)   
        print("harga makanan Rp.",totalmkn)
        tanya()
   return

def tanya():
    print("\n______________________________________________________\n")
    pertanyaan = input("Ingin memesan lagi ? y/n : ")
    print("______________________________________________________\n")
    if pertanyaan == "y":
        menu_makanan()
    elif pertanyaan == "n":
        menu_minuman()
    else:
        print("maaf anda salah menginputkan!!")
        tanya()



def menu_minuman():
   global gelas
   global totalmnm
   global mnm
   print("================= Daftar Menu minuman ================")
   print("\t |  1. es teh manis         = Rp.4.000 \t|")
   print("\t |  2. teh manis hangat     = Rp.3.000 \t|")
   print("\t |  3. es coklat            = Rp.8.000 \t|")
   print("\t |  4. jus alpukat          = Rp.10.000 |")
   print("\t |  5. jus mangga           = Rp.10.000 |")
   print("\t |  6. es kopi susu cantik  = Rp.15.000 |")
   print(baris)
   menu_minuman = int(input("Masukkan nomer menu_minuman pilihan anda  : "))
   
   if menu_minuman == 1:
        jumlah = int(input("Masukkan jumlah gelas : "))
        gelas.append(jumlah)
        totalmnm = 4000 * jumlah
        total.append(totalmnm)
        minum=("es teh manis")
        mnm.append(minum)
        print("harga minuman Rp.",totalmnm)
        tanya2()
   elif menu_minuman == 2:
        jumlah = int(input("Masukkan jumlah gelas : "))
        gelas.append(jumlah)
        totalmnm = 3000 * jumlah
        total.append(totalmnm)
        minum=("teh manis hangat")
        mnm.append(minum)
        print("harga minuman Rp.",totalmnm)
        tanya2()
   elif menu_minuman == 3:
        jumlah = int(input("Masukkan jumlah gelas : "))
        gelas.append(jumlah)
        totalmnm = 8000 * jumlah 
        total.append(totalmnm)
        minum=("es coklat")
        mnm.append(minum)
        print("harga minuman Rp.",totalmnm)
        tanya2()
   elif menu_minuman == 4:
        jumlah = int(input("Masukkan jumlah gelas : "))
        gelas.append(jumlah)
        totalmnm = 10000 * jumlah
        total.append(totalmnm)
        minum=("jus alpukat")
        mnm.append(minum)
        print("harga minuman Rp.",totalmnm)
        tanya2()
   elif menu_minuman == 5:
        jumlah = int(input("Masukkan jumlah gelas : "))
        gelas.append(jumlah)
        totalmnm = 10000 * jumlah   
        total.append(totalmnm)
        minum=("jus mangga")
        mnm.append(minum)        
        print("harga minuman Rp.",totalmnm)
        tanya2()
   elif menu_minuman == 6:
        jumlah = int(input("Masukkan jumlah gelas : "))
        gelas.append(jumlah)
        totalmnm = 15000 * jumlah   
        total.append(totalmnm)        
        minum=("es kopi susu cantik") 
        mnm.append(minum)   
        print("harga minuman Rp.",totalmnm)
        tanya2()
   return


def tanya2():
    print("\n______________________________________________________\n")
    tanya = input("Ingin memesan lagi ? y/n : ")
    print("______________________________________________________\n")
    if tanya == "y":
        menu_minuman()
    elif tanya == "n":
        akhir()
    else:
        print("maaf anda salah menginputkan!!")
        tanya2()

def akhir():
    for harga in total:
        print("Total pesanan    : ",porsi,"porsi\n\t\t",mkn)
        print("\t\t : ",gelas,"gelas\n\t\t",mnm)
        print("______________________________________________________\n")
        diskon = 5/100
        a = sum(total)
        print("Total            : ",total,"\n\t\t  =",a)
        if a > 50000:
            diskon = a * 5/100
            print("discount 5%")
        else:
            diskon = 0
            print("tidak ada discount")
        print("Diskon           : ", diskon)
        totalakhir = a - diskon
        print("Total semua      : ", totalakhir)
        print("-------------------------------")
        bayar = int(input("Bayar            :  "))
        kembalian = bayar - totalakhir
        print()
        print(baris)
        print("================= S T R U K   B E L I ================")
        print(baris)
        print()
        print ("Nama\t\t:",pembeli)
        print ("Beli\t\t:",porsi,"porsi\n\t\t",mkn)
        print("\t\t:",gelas,"gelas\n\t\t",mnm)
        print ("Tagihan\t\t: Rp",totalakhir)
        print ("Dibayar\t\t: Rp",bayar)
        print("Kembalian       : Rp", kembalian)
        print(baris)
        print("\n[terimakasih",pembeli,"telah berbelanja di Angeom store]\n")
        print(baris)
        break
		
menu_makanan()