favorite_languanges = {

	'jen' : 'python',
	'sarah' : 'c++',
	'edward' : 'ruby',
	'alex' : 'lua',
	'mike' : 'python'
}


rgb_color = (100, 200, 0)
position = (30, 100)

print(favorite_languanges.items())

for name, languange in favorite_languanges.items():
	print(f"{name.title()}'s favorite languange is {languange.title()}.")

for name in sorted(favorite_languanges.keys()):
	print(f"{name.title()}, thank you for taking the poll")

my_list = ['a', 'b', 'c', 'a']
print(set(my_list))

for languange in sorted(set(favorite_languanges.values())):
	print(f"{languange}")