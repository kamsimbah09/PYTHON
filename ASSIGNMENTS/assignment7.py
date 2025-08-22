"""
This program demonstrates a game called secret number where the user is asked to input a secret number until it matches 
what is in the system
"""
print("Guess the number")
number = input()
if number == "12":
    print("Correct!You win")
else:
    print("Guess again.")
    