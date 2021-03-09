# Program takes in input of persons height and weight
# and then outputs the calculated Body Mass Index
# Author: Oisin Casey


height = int(input("Please enter your height in cm: "))
weight = int(input("Please enter your weight in kg: "))
bmi = weight / height
#next line formats the variable bmi into a string with two numbers after the decimal point
formattedBmi = "{:.2f}".format(bmi)
print ("BMI is: " + formattedBmi + ".")