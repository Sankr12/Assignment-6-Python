# Write a python script to take the month value in numeric format and display the number of days in it

month = int(input("Enter the month number: "))

if(month==2):
    print("28 Days")
elif(month<=7 and month%2!=0):
    print("31 Days")
elif(month>=7 and month%2==0):
    print("31 Days")
else:
    print("30 Days")
print()