# Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots

print("Enter the coefficient of quadratic equation (ax^2 + bx + c)")
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

d = b*b-4*a*c

if(d>0):
    print("Real & Distinct roots")
elif(d==0):
    print("Roots are equal")
else:
    print("Roots are imaginary")

print()