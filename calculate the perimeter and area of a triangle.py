# Taking the input values from user
import math
from multiprocessing.spawn import prepare


a = float(input("Enter the first side of the triangle:"))
b = float(input("Enter the second side of the triangle"))
c = float(input("Enter the third side of triangle:"))
# calculating the perimeter
perimeter = a + b + c
print("Perimeter of triangle:", perimeter)
# using heron's formula to calculate the area
# Semiperimeter = s
s = perimeter/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle:", area)
