# Write a python script to check whether a given number is three digit or not 

num = int(input("Enter a Number: "))
a = num

num=num//100

if(0<num<10):
    print(a,"is three digit number")
else:
    print(a,"is not three digit number")
print()