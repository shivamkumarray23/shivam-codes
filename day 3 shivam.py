def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


#checking even and odd
number= int(input("Enter a number: "))
if number%2==0 :
    print("The number is even")
else:
    print("The number is odd")






number = int(input("Enter a number: "))
temp = number
rev = 0
while number!= 0:
    digit = number % 10
    rev = rev * 10 + digit
    number = number // 10
if temp == rev:
    print("palindrome")
else:
    print("not palindrome")



#TAKING INPUTS FROM USER TO CALCULATE THE AREA OF PARALLELOGRAM AND RHOMBUS
base=int(input("Enter base: "))
height=int(input("Enter height: "))
area=base*height
print("THE AREA OF PARALLELOGRAM IS :",area)
d1 = int(input("Enter length of  first diagonal: "))
d2 = int(input("Enter length of  second diagonal: "))
area1 = 1/2 * d1 * d2
print("THE AREA OF RHOMBUS IS :",area1)







#taking input users to calculate perimeter of circle triangle and rectangle
radius = int(input("Enter radius: "))
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
a=int(input("Enter length of first side of triangle:"))
b=int(input("Enter length of second side of triangle:"))
c=int(input("Enter length of third side of triangle:"))
perimeter=a+b+c
print("The perimeter of the triangle is",perimeter)
perimeter1=2*(length+breadth)
print("The perimeter of the rectangle is",perimeter1)
circumference=2*3.14*radius
print("The circumference of the CIRCLE is",circumference)




# calculate of area and volume of cubiod
l= int(input("Enter a length: "))
b = int(input("Enter a breadth: "))
h = int(input("Enter a height: "))
area = 2*l*b + 2*b*h + 2*l*h
print("THE AREA OF CUBIOD IS: ", area)
volume = (l*b*h)
print("THE VOLUME OF CUBIOD IS: ", volume)




#Taking the vaLUE FROM USER to calculate the surface area of cone and its volume
radius = float(input("Enter radius: "))
height = float(input("Enter height: "))
l = radius**2 + height**2
print(l)
surface_area = 3.14 *radius *(radius +l)
print(surface_area)
area = 3.14 * radius * radius * height * 1/3
print(area)