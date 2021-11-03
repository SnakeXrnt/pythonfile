def cetak_pilihan():
	print("pilihan menu")
	print("'c' konversi dari celcius")
	print("'f' konversi dari farenheit")
	print("'q' untuk keluar dari program")

def celcius_ke_farenhait(suhu_c):
	return 9.0 / 5.0 * suhu_c + 32 

def farenheit_ke_celcius(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0


pilihan = None
while pilihan != "q":
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