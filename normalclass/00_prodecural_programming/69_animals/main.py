import json

with open('data.json', 'r') as file:
	owners = json.load(file)

for owner, pets in owners.items():
	print(f"-{owner}")
	for pet in pets:
		print(f"\t{pet}")
	print()