def main():
	num = 10
	print(factorical(num))

def factorical(number):
	if number < 0:
		return
	if number == 0 or number == 1:
		return 1
	return number * factorical(number-1)

main()