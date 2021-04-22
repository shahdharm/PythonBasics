# Given three integers, print the smallest one.(Three integers should be user input)
x = int(input("enter the number:"))
y = int(input("enter the number:"))
z = int(input("enter the numbre:"))
if x<y and x<z:
    print(" x is smallest number:")
if y<x and y<z:
    print("y is smallest number:")
if z<x and z<y:
    print("z is smallest number:")
else:
    print()