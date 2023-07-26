# Write a python script to print greater among three numbers. Print number only once even if the numbers are the same

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(b<a>c):
    print(a)
elif(a<b>c):
    print(b)
elif(a<c>b):
    print(c)
else:
    print(a)

print()