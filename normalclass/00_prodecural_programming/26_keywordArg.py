def describe_pet(animal_type, pet_name):
	 """Display information about a pet """

	 print(f"I have a {animal_type}")
	 print(f"My {animal_type}'s name is {pet_name.title()}.")
     # . lower() , .upper()


describe_pet('hamster', 'harry') #ordered matters
describe_pet('dog', 'willie')
describe_pet(pet_name="Moiley",animal_type='pig') #unordered