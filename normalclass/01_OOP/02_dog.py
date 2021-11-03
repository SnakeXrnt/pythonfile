
class Dog:
    
    owner = 'Anas'
    
    def __init__(self,name,age):
         self.name = name 
         self.age = age 
         
         
         

cutie = Dog(name='cutie',age=0)
print(cutie.name)

babe = Dog('babe',0)
print(babe.name)

bim = Dog('bim',age=0)
print(bim.name , bim.age)

print(cutie.owner , babe.owner , bim.owner)
babe.owner = 'reni'
print(cutie.owner , babe.owner , bim.owner)
Dog.owner = 'TJ'
print(cutie.owner , babe.owner , bim.owner)



