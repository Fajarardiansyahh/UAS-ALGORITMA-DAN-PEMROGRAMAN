#hal pertama membuat user pembelian
pembelian="y"
# while adalah kode yang metode yang efektif untuk mengendalikan eksekusi berulang berdasarkan kondisi tertentu
while pembelian =="y":
    print(""" 
          WARKOP MANG ARDI
    ==========================
    1. KOPI ITEM  : Rp5000
    2. INDOCAFE   : Rp4000
    3. MIE INSTAN : Rp7000
    =========================""")

    pilihan= str(input("=====MASUKAN NOMOR MENU ===== :"))
    jumlah = int(input(" Masukan Nilai Berapa Banyak Pilihan :"))
    #IF,ELIF,ELSE ADALAH SEBUAH KONSEP DALAM PEMROGRAMAN 
    #YANG DIGUNAKAN UNTUK PENGAMBILAN KEPUTUSAN ATAU KONTROL ALIRAN PROGRAM

    if pilihan=="1":
        listnama = "KOPI ITEM"
        harga = (5000*jumlah) 
        diskon = 0
        total = (harga)
    elif pilihan=="2":
        listnama = "INDOCAFE"
        harga = (4000*jumlah) 
        diskon = 0
        total = (harga)
    elif pilihan=="3":
        listnama = "MIE INSTAN"
        harga = (7000*jumlah) 
        diskon = 0
        total = (harga)
    else :
        listname = "_"
        harga = "_"
        diskon = "_"
        pilihan = input (" Menu Tidak Ada Silahkan Masukan Menu Yang Lain")
    print ("================================================")
    print (" WARKOP MANG ARDI")
    print ("Nama Menu =",listnama)
    print ("Jumlah Pesanan",jumlah)
    print ("Harga Pesanan",harga)
    print ("================================================")
    pilihan = input ("Apakah Ada Yang Dipesan Lagi? Y/N")




      
    
    
