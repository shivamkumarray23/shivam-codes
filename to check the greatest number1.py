#taking the input fromuser to find the greatest number
a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
if a>b:
    print("The greatest number is ",a)
elif b>a:
    print("The greatest number is ",b)
else:
    print("The number is equal")