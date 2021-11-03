# This program calculates the aritmatic sequence
a = 0
b = -2
count = 0
max_count = 20

while count < max_count:
	count = count + 1
	print(a, end=" ") #Notice the magic end=" " in the print func
	                  # that keeps it from creating a new line.
    a = a + b
print() # gets a new (empty) line.