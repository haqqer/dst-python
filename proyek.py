from random import random 	#Untuk mengimport fungsi random
import math 	#untuk mengimport class math 

angka_kunci = math.ceil(random()*100) 	#math.ceil berfungsi untuk membulatkan angka random
print("Aku adalah angka antara 1 - 100")
sisa_tebakan = 10 	#sisa tebakan untuk user
i=0 


while i == 0: 	#looping tebakan apabila tebakan sisa_tebakan habis looping berhenti
	tebak = input("Masukan tebakan mu : ") 	#menginput angka tebakan mu
	if(tebak<angka_kunci): 	#apabila tebakan lebih kecil dari angka kunci
		print("Tebakan terlalu rendah") 
		sisa_tebakan-=1 	#sebab salah, angka kita kurangi sisa_tebakan
		print("Sisa Tebakan %d" % sisa_tebakan)
		if(sisa_tebakan<1): 		#apabila sisa_tebakan kurang dari satu
			print("Anda Kalah, jawaban = %d" % angka_kunci) 	#maka permainan selesai
			i=1

	elif(tebak>angka_kunci): 	#apabila tebakan lebih kecil dari angka kunci
		print("Tebakan terlalu tinggi")
		sisa_tebakan-=1 	#sebab salah, angka kita kurangi sisa_tebakan
		print("Sisa Tebakan %d" % sisa_tebakan)
		if(sisa_tebakan<1): 	#apabila sisa_tebakan kurang dari satu
			print("Anda Kalah, jawaban = %d" % angka_kunci)
			i=1
	else:
		print("Selamat Anda Menang") #apabila tidak ada koreksi maka anda menang
		i=1