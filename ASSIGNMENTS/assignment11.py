"""
This program demonstrates a simple yes or no
It keeps asking the user if he/she wants to continue,they will choose Y to continue but N to end the program.
"""
while True:
    num = int(input("Enter a number:"))

    print("You entered:",num)

    choice = input("Do you want to continue?(Y/N):")

    while choice not in ['Y','N']:
        choice = input("Invalid choice")

    if choice == 'N':
        print()    