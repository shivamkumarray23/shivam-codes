
x = [1 ,2, 3]
y = [1 , 2 ,3]
z = x
print(x is z)

print(x is not y)



x = 10
print(x)
x +=3 #x=x+3
print(x)
x -=3 #x=x-3
print(x)
x *=3 #x=x*3
print(x)
x /=3 #x=x/3
print(x)

#shifting
import math
from math import floor
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = x & y
print(z)
a = x | y
print(a)
b = (-(x +1 ))
print(b)
c = x ^ y
print(c)
d = x >> y
print(d)
e = x << y
print(e)
f= floor(x/2**y)
print(f)
g = x * (2 ** y)
print(g)

#logical operation
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = x and y
a = x or y
b = not x
c = not y
d = not x or not y
print(z)
print(a)
print(b)
print(c)
print(d)



 # relational condition
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = x==y
a = x != y
b = x > y
c = x < y
d = x >= y
e = x<= y
print(z)
print(a)
print(b)
print(c)
print(d)
print(e)

#mathematical operation
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
sum = a + b
sub = a - b
mul = a * b
div = a / b
mod = a % b
floordiv = a // b
exponent = a ** b
print(sum, sub, mul, div, mod, floordiv, exponent)

# TypeConversion
#1. Implict conversion
x = 5
y = 2.5
sum = x + y
print(sum)

# Explict conversion
x = "10"
y = x +5
print(y)
y1 = int(x)+5
print(y)
print(y1)







from operator import truediv
from pkg_resources import non_empty_lines

x = 4 #int
y = 4.18 #float
z= 3 + 4j #complex
print(x)
print(y)
print(z)

name = "Alice" #string
print(name)


my_list = [1,2,3,4,5,6,7,8,9]
print(my_list)
my_tuple = (1,2,3,4,5,6,7,8,9)
print(my_tuple)
my_range = range(1,10)
print(my_range)


details = {"name" : "Alice","age" :18}
print(details)


my_set = {1,2,3,4,5,6,7,8,9}
print(my_set)
my_frozenset = frozenset({1,2,3,4,5,6,7,8,9})
print(my_frozenset)

nothing = None
print(nothing)
