name = input()
my_number = 0
for char in name.upper():
	my_number += ord(char)
#print(my_number)
print("Inisial Jodoh Kamu : ", chr(my_number%26 + 65))7