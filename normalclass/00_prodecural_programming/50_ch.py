"""
#1
manusia = [
{'color':'hitam', 'duit':100000, 'nama':'Michael'},
{'color': 'putih', 'duit':80000, 'nama':'Alex'},
{'color': 'krem', 'duit':70000, 'nama':'Steve'}
]

for orang in manusia:

	for key,val in orang.items():
		print(f"{key} \t:{val}")

	print()
#2
hewan = [
{'color':'coklat', 'makanan':'Daging', 'milik':'Ahmad'},
{'color': 'putih', 'makanan':'Daging', 'milik':'Udin'},
{'color': 'coklat tua', 'makanan':'Daging', 'milik':'Martin'},
{'color': 'coklat tua', 'makanan':'Daging', 'milik':'Steven'}
]

for peliharaan in hewan:

	for key,val in peliharaan.items():
		print(f"{key} \t:{val}")

	print()
#3
cities = [
{'kota':'Palembang', 'makanan':'pempek', 'provinsi':'Sumsel'},
{'kota': 'Jakarta', 'makanan':'kerak telor', 'provinsi':'Jakarta'},
{'kota': 'Jayapura', 'makanan':'papeda', 'provinsi':'Papua'},
{'kota': 'Banda Aceh', 'makanan':'mie aceh', 'provinsi':'Aceh'},
]

for city in cities:

	for key,val in city.items():
		print(f"{key} \t:{val}")

	print()