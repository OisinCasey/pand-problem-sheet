# Program takes positive float as input and outputs an
# approximation of its square root to one decimal place
# using the newton method of estimating square roots
# Author: Oisin Casey


def squareRoot(n, t) :

    x = n
    #count number of iterations
    count = 0

    while (1):

        count += 1
        root = 0.5*(x + (n /x))

        # checks the closeness of the estimate, if difference is less than 1 it breaks
        if (abs(root - x) < t):
            break
        #update square root value
        x = root
    return root
 # ask user for number to find/estimate root of
numberToRoot = float(input("Please enter a positive number: "))
limit = 0.1
rootAns = squareRoot(numberToRoot, limit)

# print answer with formatting to one decimal place
print("The square root of {} is approx {:.1f}".format(numberToRoot ,rootAns))
