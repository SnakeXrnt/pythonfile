def oneToTen(init, final)):
	print(init, end=" ")
	if init <= 10:
		return oneToTen(init+1, final)
	print()

def oneToTenWhile(init, final):
	while init < final:
		print(init, end=" ")
	print()

oneToTen(1, 10)
oneToTenWhile(1, 10)