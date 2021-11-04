
class Car:
    
    def __init__(self,make,model,year,color,new,manual):
        
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.new = new
        self.manual = manual
        
    def get_descriptive(self):
        return f'Merek Mobil\t: {self.make}.\nJenis Mobil\t: {self.model}. '