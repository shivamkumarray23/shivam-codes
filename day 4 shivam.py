#write the programes to find the roots of quadratic equation
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter another number: "))
root1=((-b)+(b**2-4 * a * c)**0.5)/2*a
root2=((-b)-(b**2-4 * a * c)**0.5)/2*a
print("root1",root1)
print("root2",root2)









#write a program to add two complex number
a=complex(input("Enter a first number: "))
b=complex(input("Enter a second number: "))
print(a+b)





























#write a program to determine if a triangle is valid based on length of its side
a=int(input("Enter a first side of triangle: "))
b=int(input("Enter a second side of triangle: "))
c=int(input("Enter a third side of triangle: "))
if a<=0 or b<=0 or c<=0:
    print("Please enter all values")
else :
    if ((a+b>c) and
          (a+c>b) and
            (b+c>a)):
        print("Triangle is valid.")
    else:
        print("Triangle is  not valid.")













#write a program to calculate the electricity bills by following rules ; 1 st hundered unit be 0.5 dollar next 100 units charged be 0.75 unit and above 200 1 dollar
unit=float(input("enter your units: "))
if unit>0 and unit ==100:
    bill=0.5*unit
    print("bill is ",bill,"$")
elif unit>100 and unit<200:
    bill=0.75*(unit-100)+0.5*100
    print("bill is ",bill,"$")
elif unit>200:
    bill=1*(unit-200)+0.5*100+0.75*100
    print("bill is ",bill,"$")



















#Entered character is vowel or cosonant
char = input("Enter a character: ")
if len(char) == 1 and char.isalpha():
    if char in "aeiou":
        print(f"{char} is an vowel.")
    else :
        print(f"{char} is consonant.")
















#write a program to check the character is vowel or consonant
str=input("enter any word: ")
if str=="a":
    print("vowel")
elif str=="e":
    print("vowel")
elif str=="i":
    print("vowel")
elif str=="o":
    print("vowel")
elif str=="u":
    print("vowel")
else:
    print("consonant")




















 #write a program to categories child(0-12) teenager(13_19) ADULT(20-59) and senior(60+0)
age=int(input("enter your age: "))
if age>=0 and age<=12:
 print("he is child")
elif age>=13 and age<=19:
 print("he is teenager")
elif age>=20 and age<=59:
 print("he is adult")
elif age>=60:
    print("he is senior")















 #check a number divisible by 3 and 5 both
number=int(input("Enter a number: "))
if number%3==0 and number%5==0:
    print("The number is divisible by 3 and 5")
else :
    print("The number is not divisible by 3 or 5")


















 # Simple calculator making
num1=float(input("Enter a number: "))
num2=float(input("Enter a number: "))
ope=(input("Enter operator: {+, _, *, / < %"))
if ope=="+":
    print(num1+num2)
elif ope=="-":
    print(num1-num2)
elif ope=="*":
    print(num1*num2)
elif ope=="/":
    print(num1/num2)
elif ope=="%":
    print(num1/num2)


































 #checking the year is leap year
year=int(input("Enter year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")



# checking year is leap year
year=int(input("Enter year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("the year is a leap year")
else:
    print("the year is not a leap year")

  #Marks information
marks=int(input("Enter marks: "))
if marks >= 85:
    print("Your grade is A")
elif marks >= 75:
    print("Your grade is B")
elif marks >= 65:
    print("Your grade is C")
elif marks >= 55:
    print("Your grade is D")
elif marks >= 35 :
    print("Your grade is F")
else:
    print("Your grade is fail")






#write a program to print to you are eligible for vote if you are 18+ and citizen of indian:
age=int(input("enter your age"))
citizen=input("enter your citizen")
if age>=18:
    if citizen=="india":
     print("you are Eligible for vote")
else:
    print("you are not Eligible for vote")



#checking the number is positive number or negative number
number=int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
   print("The number is zero.")


#checking number is even or odd
number=int(input("Enter a number: "))
if number%2==0:
    print("The number is Even")
else:
    print("The number is Odd")

#checking for vote
age=int(input("enter your age"))
if age>=18:
    print("you are Eligible for vote")
else:
    print("you are not Eligible for vote")


# checking number is negative number
number1=int(input("Enter a number: "))
if number1< 0:
    print("The number is negative.")

#checking the number is positive number
number=int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")



#checking number is odd
number = int(input("Enter a number: "))
if number % 2!=0:
    print(" the number is odd")



#checking number is even
number=int(input("Enter a number: "))
if number%2==0:
    print("The number is Even")

#checking age foreligible for vote
age=int(input("enter your age"))
if age>=18:
    print("you are Eligible for vote")
else:
    print("you are not Eligible for vote")