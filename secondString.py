# This program reads in a string and
# outputs every second letter in 
# reverse order
# Author: Oisin Casey

inString = input("Please enter a sentence: ")

reverseString  = inString[::-1] #this reverses the order of the string
outString =  reverseString[::2]  #this outputs every other letter of the string starting at the first


print(outString)
