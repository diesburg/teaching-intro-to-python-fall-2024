"""
File: calculator.py
code: Levi Bostian bostianl@uni.edu
Description: Intro to Computing Fall 2014 assignment 2 part 2
"""

operand1 = int(input("What is the first integer value? "))
operand2 = int(input("What is the second integer value? "))
operator = input("What operation are you performing? ")

if operand1 <= 0 or operand1 >= 100:
    print("The first integer value is invalid.")
elif operand2 <= 0 or operand2 >= 100:
    print("The second integer value is invalid.")
else:
    if operator == "+":
        print("Answer: " + str(operand1 + operand2))
    elif operator == "-":
        print("Answer: " + str(operand1 - operand2))
    elif operator == "*":
        print("Answer: " + str(operand1 * operand2))
    elif operator == "/":
        print("Answer: " + str(operand1 / operand2))
    elif operator == "//":
        print("Answer: " + str(operand1 // operand2))
    elif operator == "%":
        print("Answer: " + str(operand1 % operand2))
    elif operator == "**":
        print("Answer: " + str(operand1 ** operand2))
    else:
        print("You entered an invalid operator.")
