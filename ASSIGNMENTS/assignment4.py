"""
This program demonstrates a password checker where the user inputs their password and it checks if it correct or not
"""
print("What is your password?")
password = input()

if password.upper() == "MR FRANK":
    print("Access Given")
else:
    print("Access Denied")