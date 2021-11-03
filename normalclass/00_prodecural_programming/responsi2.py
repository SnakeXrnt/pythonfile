#makanan = ['Ayam goreng', 'Ikan Gurami', 'Udang goreng', 'Cumi Goreng', 'Nasi Goreng']
makanan = ['Ikan Gurami', 'Ayam Goreng', 'Nasi Goreng', 'Cumi Goreng', 'Udang goreng']
print(makanan)

makanan[0] = 'Ayam goreng'
print(makanan)

makanan.pop(0)
print(makanan)

makanan.pop(3)
print(makanan)

#teman memberi uang untuk pecel lele
makanan.append('Pecel lele')
print(makanan)

makanan.insert(0, 'Pecel lele')
print(makanan)

makanan.pop(4)
print(makanan)