import math
print("*************************************")
print("Solving Second Degree Equations")
print("*************************************\n")

a = float(input("Type the value of a: "))
b = float(input("Type the value of b: "))
c = float(input("Type the value of c: "))

delta = b*b - 4*a*c
if delta>0:
    print("\nTwo real roots")
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print(x1, x2)
if delta<0:
    print("\nThere aren't real roots")

