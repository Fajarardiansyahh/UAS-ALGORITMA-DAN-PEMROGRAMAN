print("PROGRAM HITUNG GAJI KARYAWAN")
#TUN.JABATAN
#GOL : 1 = 5%(0.05), 2 = 10% (0.10), 3 = 15%(0.15)
#TUN.PEN
#PENDIDIKAN: SMA = 2.5%(0,25), D1 = 5%(0.05), D3 =20%(0.02)
#S1= 30%(0.3)
#LEMBUR
#MORE THAN 8H = 3500/HOUR
nakar = input("nama :")
golonga_jabatan = input("Golongan Jabatan [1/2/3]: ")
pendidikan = input ("Pendidikan [SMA/D1/D3/S1]: ")
#IF,ELIF,ELSE ADALAH SEBUAH KONSEP DALAM PEMROGRAMAN
#YANG DIGUNAKAN UNTUK PENGAMBILAN KEPUTUSAN ATAU KONTROL ALIRAN PROGRAM
if golonga_jabatan == "1":
   jabatan = 300000*0.05
   if pendidikan == "SMA" or pendidikan == "sma":
      tunjangan =300000*0.025
elif pendidikan == "D1" or pendidikan == "d1":
       tunjangan = 300000*0.05
elif pendidikan == "D3" or pendidikan == "d3":
     tunjangan = 300000*0.02
if golonga_jabatan == "2":
   jabatan = 300000*0.10
   if pendidikan == "SMA" or pendidikan == "sma":
      tunjangan =300000*0.025
elif pendidikan == "D1" or pendidikan == "d1":
       tunjangan = 300000*0.05
elif pendidikan == "D3" or pendidikan == "d3":
     tunjangan = 300000*0.02
if golonga_jabatan == "3":
   jabatan = 300000*0.15
   if pendidikan == "SMA" or pendidikan == "sma":
      tunjangan =300000*0.025
elif pendidikan == "D1" or pendidikan == "d1":
       tunjangan = 300000*0.05
elif pendidikan == "D3" or pendidikan == "d3":
     tunjangan = 300000*0.02
jamkerja = int(input("Jumlah Jam Kerja :"))
if jamkerja >8:
     total = (jamkerja - 8 )*3500
else :
     total = 0
x = 300000+jabatan+tunjangan+total
print("")#bari baru
print("karyawan yang bernama :", nakar)
print("honor yang diterima")
print("tunjangan jabatan Rp.", jabatan)
print("tunjangan pendidikan RP.",tunjangan)
print("honor lembur Rp.", total)
print("Total Gaji Rp. %.0f"%x)
     


 