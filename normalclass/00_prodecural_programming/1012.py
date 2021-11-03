a, b, c = input().split(" ")
a, b, c = flaot(a), float(b), float(c)

triangle = float(a) * float(c)/2
circle = float(c) * 3.14159 * float(c)
tra = float(a) * (float(c) + float(b)) / 2
square = b * b
rect = a * b

print("TRIANGULO: {triangle:.3f}\nCIRCULO: {circle:.3f}\nTRAPEZIO: {tra:.3f}\nQUADRADO: {square:.3f}\nRETANGULO: {rect:.3f}\n")