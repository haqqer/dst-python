

n_tgs = input("Masukan nilai tugas = ")
n_uts = input("Masukan nilai UTS = ")
n_uas = input("Masukan nilai UAS = ")

n_akhir = (n_tgs*0.4)+(n_uts*0.3)+(n_uas*0.3)

if n_akhir >= 85:
	print("Grade Nilai Anda A ")
	print("Nilai Akhir : "+str(n_akhir))
elif n_akhir >= 70 and n_akhir < 85:
	print("Grade Nilai Anda B")
	print("Nilai Akhir : "+str(n_akhir))
elif n_akhir < 70:
	print("Grade Nilai Anda C")
	print("Nilai Akhir : "+str(n_akhir))