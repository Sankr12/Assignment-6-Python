# Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part

# Input a complex number from the user
complex_num_str = input("Enter a complex number (in the form 'a+bj' or 'a-bj'): ")

# Convert the input string to a complex number
try:
    complex_num = complex(complex_num_str)
    real_part = complex_num.real
    imag_part = complex_num.imag
    
    if real_part > imag_part:
        print("The real part is greater:", real_part)
    elif imag_part > real_part:
        print("The imaginary part is greater:", imag_part)
    else:
        print("The real and imaginary parts are equal:", real_part)

except ValueError:
    print("Invalid input! Please enter a valid complex number.")
