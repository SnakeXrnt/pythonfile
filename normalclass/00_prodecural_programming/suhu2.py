import os 

def cetak_pilihan():
	print("pilihan menu")
	print("'cf' konversi dari celcius-farenheit")
	print("'cr'")
	print("'ck'")
	print("'fc' konversi dari farenheit-celcius")
	print("'fr'")
	print("'fk'")
	print("'rf'")
	print("'rc'")
	print("'rk'")

	print("'q' untuk keluar dari program")
#c:r:f:k = 5:4:9(+- 32):5 (+- 273)
def celcius_ke_farenhait(suhu_c):
	return 9.0 / 5.0 * suhu_c + 32 

def celcius_ke_reamur(suhu_c):
	return 4.0 / 5.0 *suhu_c

def farenheit_ke_celcius(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0

def reamur_ke_kelvin(suhu_r):
	return 5.0/4.0 * suhu_r + 273

def reamur_ke_farenheit(suhu_r):
	return 9.0/4.0 * suhu_r + 32

def farenheit_ke_reamur(suhu_f):
	return (suhu_f - 32) * 4.0 / 9.0

def
error = False
pilihan = None
while not error:
	os.system("clear")
	cetak_pilihan()
	pilihan = input("pilihan : ")
	if pilihan == 'c':
		main_c = float(input("suhu celcius-nya : "))
		result = celcius_ke_farenheit(main_c)
		print(f"farenheit : {resut}")
	elif pilihan == 'f':
		main_f = float(input("suhu farenheit-nya : "))
		print(f"celcius : {farenheit_ke_celcius(mian_f)}")
print("bye bye...")