"""
1. Bayangkan kita akan pergi ke 5 tempat baru
2. Buatkan lists dari 5 tempat tersebut dan tidak perlu terurut
3. Cetak lists yg original
4. Cetak lists terurut tanpa mengubah list yg asli
5. Karena dana terbatas hapus 2 tujuan yang pertama hapus item di index 3,yang kedua hapus index terakhir
6. Tiba-tiba ada sponsor yg mendanai pergi ke paris,masukkan kota paris sebagai tujuan pertama di list.
7. cetak list setelah diurutkan permanen dan secara decending (Z-A)
dikumpul di moodle gunakan link pastebin
"""

#tempat tujuan = ['Malaysia', 'Taiwan', 'Singapore', 'Jepang', 'Thailand']
tempat_tujuan = ['Singapore', 'Malaysia', 'Taiwan', 'Jepang', 'Thailand']
print(tempat_tujuan)

tempat_tujuan[0] = 'Malaysia'
print(tempat_tujuan)

tempat_tujuan.pop(0)
print(tempat_tujuan)

tempat_tujuan.pop(3)
print(tempat_tujuan)

#ada yang mendanai ke Paris
tempat_tujuan.append('Paris')
print(tempat_tujuan)

tempat_tujuan.insert(0, 'Paris')
print(tempat_tujuan)

tempat_tujuan.pop(4)
print(tempat_tujuan)

tempat_tujuan.sort(descend=True)
print(tempat_tujuan)