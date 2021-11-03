
class Dog:

    def __init__(self,name): #fungsi constructor 
        self.name = name
        self.age = 0 
        self.isCute = True
        self.tj_eat()
        
    def tj_eat(self):
        to_be_print = self.name + ' is eating DogFood "Rawrrr"'
        print(to_be_print)

Faris = Dog('Faris')
print(Faris.name)
print(Faris.age)
print(Faris.isCute)

holy = Dog('TJ')
print(holy.name)