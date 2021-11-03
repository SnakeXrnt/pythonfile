from math import sin, pi, radians
from random import randint
from datetime import datetime as dt

def sin_versi_saya(angle):
	return sin(radians(angle))

def lempart_dadu():
	return randint(1,6)

"""
print(sin(pi/6))
print(sin(radians(30)))
print(sin_versi_saya(30))
"""

print(lempart_dadu())
print(dt.now().year)