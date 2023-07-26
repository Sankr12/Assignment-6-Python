# Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))

if(num1>num2):
    print(num1)
elif(num1==num2):
    print(num1)
else:
    print(num2)