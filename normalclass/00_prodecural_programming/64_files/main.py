
with open('data.txt', 'r') as file:
	fruits = file.readlines()

print(fruits)
our_fruits = fruits.split("\n")
print(type(fruits))