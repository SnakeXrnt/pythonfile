available_toppings = ['mushroom', 'olives', 'pepperoni', 'pineapple', 'cheese']

requested_toppings = []
stop = False
while not stop:
	topping = input("Input your topping here ('q' to  quit.): ")
	if topping != 'q':
		requested_toppings.append(topping)
	else:
		stop = True

for requested_toppings in requested_toppings:
	if requested_toppings in available_toppings:
		print(f"Adding {requested_toppings}.")
	else:
		print(f"Sorry, we dont have {requested_toppings}")

print("\nFinished making your pizza.")