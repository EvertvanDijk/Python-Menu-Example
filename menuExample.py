import os
# Define some colours in def
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

# Create the functions
def AddUp(a,b):
    return int(a) + int(b)

def Multiply(a,b):
    return int(a) * int(b)

def Divide(a,b):
    return int(a) / int(b)

# Clear the screen (for readability)
os.system('cls')

# Text in Yellow for easier reading on Black background
prYellow("This Program will Calculate 2 numbers of your choice according to the numerator you also choose.")
prYellow("Please enter your numbers and then hit the Enter key, followed by either the plus, Multiply or divide sign.")
# Ask for the numbers and sign
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
Choice = input("Please choose one of the following signs: '+' '*' or '/' :")

# Switch and outputs
if Choice == "+":
    prRed("If you add " + str(num1) + " and " + str(num2) + " you get: " + str(AddUp(num1, num2)))
elif Choice == "*": 
    prRed("If you multiply " + str(num1) + " and " + str(num2) + " you get: " + str(Multiply(num1, num2)))
else:
    prRed("If you divide " + str(num1) + " and " + str(num2) + " you get: " + str((num1, num2)))
