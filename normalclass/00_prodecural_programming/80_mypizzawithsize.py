
def make_pizza(size, *toppings):
	print(f"\nMaking a {size} cm pizza with the following toppings : ")
	if toppings:
		for topping in toppings:
			print(f"\t-{topping}")
	else:
		print("There is no topping.")
	#print("Your Toppings :",toppings)

make_pizza(12)
make_pizza(15, "extra chili,cheese")
make_pizza(18, "not hot", "cheese", "mushrooms", "pepperoni")