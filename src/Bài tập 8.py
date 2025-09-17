# ▸Write a Python program:
# 1.to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

# 2.that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    num = int("abc")
    print("Number:", num)
except ValueError:
    print("Error: That is not a valid integer!")

# 3.that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    a = "hello"
    b = 5
    result = a + b
    print("Sum:", result)
except TypeError:
    print("Error: Both inputs must be numerical!")

# 4.that executes an operation on a list and handles an IndexError exception if the index is out of range.
numbers = [1, 2, 3]
try:
    print(numbers[5])  # out of range
except IndexError:
    print("Error: Index is out of range!")

# 5.that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    num = input("Enter a number (press Ctrl + C to cancel): ")
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nError: Input was cancelled by user!")

# 6.that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ArithmeticError:
    print("Error: An arithmetic error occurred!")