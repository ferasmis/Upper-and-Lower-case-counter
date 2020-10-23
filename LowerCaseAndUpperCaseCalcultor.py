## Author: Feras
## Problem: Write a function that accepts a string and calculate 
##      the number of upper case letters and lower case letters.


def lowerAndUpperCaseCalculator():
    counterUpperCase = 0
    counterLowerCase = 0
    string = input("Enter a sentence:\n")
    for i in string :
        if i in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            counterUpperCase += 1
        elif i in ('abcdefghijklmnnopqrstuvwxyz'):
            counterLowerCase += 1
    print("Number of upper case letters are " + str(counterUpperCase) + "."
    + " Number of lower case letters are " + str(counterLowerCase))
lowerAndUpperCaseCalculator()