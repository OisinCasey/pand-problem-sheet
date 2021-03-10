# When run, the program tells the user whether
# today is a weekday or not
# Author: Oisin Casey

# import pythons datetime module

import datetime

# The weekday() function of date class in datetime module, returns an integer
# corresponding to the day of the week
# monday is 0 and sunday is 6


# check if today is a weekday less than 5, i.e. saturday
if (datetime.datetime.today().weekday() < 5):
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
