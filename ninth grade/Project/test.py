from json import *


barang = open('barang.json','r+')
dictbar = load(barang)


keylist = list(dictbar.keys())
keysavia = len(keylist)
print(keysavia)
counter = 0
print(keylist)
for x in range(len(keylist)):
    keyonebyone = keylist[x]
    nama = dictbar[keyonebyone]['nama']
    jumlah = dictbar[keyonebyone]['jumlah']
    tanggal = dictbar[keyonebyone]['tanggal']
    all = 'nama:' + nama +'jumlah :'+ jumlah +'tanggal : '+ tanggal
    print(all)
