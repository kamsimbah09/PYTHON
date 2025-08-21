"""
This program demonstrates the greater of two numbers based on the input of the user
"""

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))


if num1 > num2:
    print(f"The greater number is {num1}")
else:
    if num2 > num1:
        print(f"The greater number is {num2}") 