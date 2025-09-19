"""
This program demonstrates basic arithmetic operations
using two variables: addition, subtraction, multiplication, and division.
It prints out the results with descriptive text.
"""

while True:
# Define the two variables
 num1 = int(input("Enter your first number:"))
 num2 = int(input("Enter your second number:"))

# Addition
 #sum_result = num1 + num2
 #print(f"This is the sum of the two numbers: {sum_result}")



# Subtraction
 #sub_result = num1 - num2
 #print(f"This is the subtraction of the two numbers: {sub_result}")

# Multiplication
 #mul_result = num1 * num2
 #print(f"This is the multiplication of the two numbers: {mul_result}")

# Division
 #div_result = num1 / num2
 #print(f"This is the division of the two numbers: {div_result}")

#assignment 2
 print("Which arithmetic operation do u want to run? addition, subtarction,multiplication,division")
 operation =input()



 if operation.lower() == "addition":
    sum_result = num1 + num2
    print(f"This is the sum of the two numbers: {sum_result}")
 else:
    if operation.lower() == "subtraction":
       sub_result = num1 - num2
       print(f"This is the subtraction of the two numbers: {sub_result}")
    else:
        if operation.lower() == "multiplication":
          mul_result = num1 * num2
          print(f"This is the multiplication of the two numbers: {mul_result}")
        else:
           if operation.lower() == "division":
              if num2 != 0:
                 div_result = num1 / num2
                 print(f"This is the division of the two numbers: {div_result}") 
              else:
                 print("Division is  not allowed")
           else:
              print("invalid operation.")  
           select = input("Do u want to continue? y OR n")  
           if select == "y":
              continue
           else:
              if select == "n":
                 break
