# This program asks for an input number and outputs the
# values for the following calculation:
# if number is even, divide by 2, if odd multiply by 3, end 
# if value is 1
# Author: Oisin Casey

number = int(input("Please enter a positive integer:"))

while number != 1:
    print(number)
    if (number % 2) == 0:
        number  = int(number / 2)
    else:
        number = int(number * 3)+1

print("The calculation is finished")