# TAKING THE INPUTS FROM THE USER TO FIND THE AREA OF RIGHT ANGLED TRIANGLE
import math
base= int(input("Enter base: "))
perpendicular= int(input("Enter perpendicular: "))
hypotenuse = (base**2 + perpendicular**2) ** 0.5
print("The hypotenuse of triangle is", hypotenuse)
area = (base * perpendicular) / 2
print("The area of triangle is", area)




#Input the radius to calcualte the area of cylinder
import math
radius = float(input("Enter radius: "))
height = float(input("Enter height: "))
volume = 3.14 * radius * radius *height
print("The volume of cylinder is", volume)
area = 2 * 2.14 * radius * (radius + height)
print("The area of cylinder is", area)



# to calculate the simple interest
import math
principal = float(input("Enter the principal: "))
time = float(input("Enter the time: "))
rate = float(input("Enter the rate: "))
SI = principal * time * rate /100
print("The simple interest is:",SI)
Amount = principal *(1 + rate / 100) ** time
CI = Amount-principal
print("The complex interest is:",CI)



#Taking the inputs from the user to chabge the temperature celsius into fahrenhit
c = float(input("Enter the temperature in Celsius: "))
f = 9/5 * c + 32
print("The temperature in Fahrenheit is:", f)




#Taking inputs from users to calcualte the perimeter and area of triangle
import math
a = int(input("Enter the length of first side of triangle: "))
b = int(input("Enter the length of second side of triangle: "))
c = int(input("Enter the length of third side of triangle: "))
s=(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
area1 = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle is:", area)
print("The area of the triangle is:", area1)



#Taking inputs from user to find the factorial
number = int(input("Enter a number: "))
factorial = 1
i = 1;
while i <= number :
    factorial = factorial * i
    i = i + 1
    print(factorial)


 # Taking inputs from the users to check the followwing number is armstrong
num = int(input("Enter a number: "))
temp = num
sum = 0
while num != 0:
    div = num % 10
    sum = sum + (div * div * div)
    num = num // 10
if temp == sum:
        print("Number is Armstrong")
else:
        print("Number is not Armstrong")


 #Taking a number from users to checkthe number is greatest
a= int(input("Enter a first number: "))
b= int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
if a>b and a>c:
    print(a)
if b>c and b>a:
    print(b)
if c>a and c>b:
    print(c)
if a == b and b == c:
    print("equal")


#Taking a number from users to checkthe number is greatest
a= int(input("Enter a first number: "))
b= int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
print(max(a,b,c))


#Taking a input from the user to check the number is divisible by 7
number = int(input("Enter a number: "))
d = 'divisible by 7' if number % 7 == 0 else 'not divisible by 7'
print(d)



#Taking radius from the users
import math
radius = float(input("Enter radius: "))
area = math.pi * (radius ** 2)
perimeter = 2 * math.pi * radius
print("Area of circle:", area)
print("Perimeter of circle:", perimeter)

# Taking radius from the users
radius = float(input("Enter radius: "))
area = 3.14 * radius * radius
perimeter = 2 * 3.14 * radius
print("Area of circle:", area)
print("Perimeter of circle:", perimeter)


print("Hello world")

#taking the values from the users
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
a = a^b
b = a^b
a = a^b
#Printing a swapped result
print(a)
print(b)

#taking the values from the users
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
a = a*b
b = a/b
a = a/b
print(a)
print(b)

#Taking the input from users for the sum of two numbers
num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
#Finding the sum of two numbers
sum = num1 + num2
avg = (num1+num2)/2
#print the sum of two numbers
print(sum)
print(avg)

#Taking the inputs from users for the swap the number USING THIRD VARIABLE
num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
temp = num1
num1 = num2
num2 = temp
print(num1)
print(num2)

#tAKING the inputs from the users for the swap the number without using third variable
a = int(input("enter num1:"))
b = int(input("enter num2:"))
a = a+b
b = a-b
a = a-b
#printing the swapped number
print(a)
print(b)
