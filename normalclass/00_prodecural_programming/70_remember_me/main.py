import json

filename = 'user.json'
try:
	with open(filename, 'r') as file:
		user = json.load(file)
except:
	user = input("Who are you ? ")

	with open(filename, 'w') as file:
		json.dump(user, file)
	print(f"I ll remembber you when you come back, bye!")
else:
	print(f"Welcome back {user}!")