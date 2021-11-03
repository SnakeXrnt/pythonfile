import json

with open('data.json', 'w') as file:
	numbers = [3, 1, 4, 1, 5, 9]
	json.dump(numbers, file)