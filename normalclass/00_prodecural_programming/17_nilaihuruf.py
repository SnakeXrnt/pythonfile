"""
Guru akan memberikan nilai huruf ke siswa
dengan aturan sb. berikut
A >= 90
B >= 80
C >= 70
D >= 65

input:
Nilai angka : 85

output:
B
Ketik program dibawah ini.
"""

nilai = int(input("Nilai berapa : "))

#bottom to top
if nilai  A:
	print("90")
elif nilai > B:
	print("80")
elif nilai > C:
	print("70")
else:
	print("65")


	#top to bottom
if nilai < C:
	print("65")
elif nilai < B:
	print("70")
elif nilai < A:
	print("80")
else:
	print("90")