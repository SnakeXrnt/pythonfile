#Changing Adding Removing Elements

motor = ['honda legenda', 'yamaha fizr', 'suzuki shogun']
print(motors)
#chaging / modifying
motors[1] = 'ducati'
print(motors)

#adding element
motors.append('kawasaki')
print(motors)

#inserting element
motors.insert(0, 'tvs')
print(motors)

motors.inser(2, 'viar')
print(motors)

#removing
motors.pop(2)
print(motors)

motors.remove('tvs') # menggunakan value
print(motors)

del motors[0]
print(motors)