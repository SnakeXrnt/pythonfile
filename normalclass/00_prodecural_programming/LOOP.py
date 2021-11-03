a = 1
s = 0
print('Masukkan angka selain angka 0 untuk memulai')
print('Masukkan 0 untuk berhenti')
while a != 0:                           
    print('Angka:', s)            
    a = float(input('Number? '))        
    s = s + a                            
print('Total Sum =', s)