
def make_pizza(*toppings):
	print("Making a pizza with the following toppings : ")
	if toppings:
		for topping in toppings:
			print(f"\t-{topping}")
	else:
		print("There is no topping.")
	#print("Your Toppings :",toppings)

make_pizza()
make_pizza("cheese")
make_pizza("cheese", "mushrooms", "pepperoni")