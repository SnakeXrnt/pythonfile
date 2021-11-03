#import math #X^2 + 5x + 6 = 0
from math import sqrt

a = float(input("koef a :"))
b = float(input("koef b :"))
c = float(input("koef c :"))
D = (b**2) - (4*a*c)
x1 = (-b + sqrt (D))/(2*a)
x2 = (-b + sqrt (D))/(2*a) 
print("Akar X1 =", x1)
print("Akar X2 =", x2)