
class Dog:

    def __init__(self,name,age,isCute): #fungsi constructor 
        self.name = name
        self.age = age
        self.isCute = isCute
name_input = input('name : ')
age_input = input('age : ')
is_cute = input('is the dog cute (y/n)')

is_cute_bolean = False

if is_cute == 'y':
    is_cute_bolean == True
else: 
    pass

Faris = Dog(name_input,age_input , is_cute_bolean)
print('Name Dog : ',Faris.name)
print('Age Dog : ',Faris.age)
if Faris.isCute == True: 
    print('this dog is cute')
else : 
    print('This Dog Is Not Cute Belog To Trash')









'''






holy = Dog('TJ', 5 , True)
print('Name Dog : ',holy.name)
print('Age Dog : ',holy.age)
if holy.isCute == True: 
    print('this dog is cute')
else : 
    print('This Dog Is Not Cute Belog To Trash ')
    '''