# Given a positive real number, print its fractional part.

import math
a=float(input("enter the number: "))
math.modf(a)
x,y=math.modf(a)
print(x)
print(y)