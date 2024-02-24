# Import libraries used in code
import random
import string
import time
import sys

# Defines the function used to generate the password after all input has been taken.
def generatePassword(length, upper, lower, numbers, symbols):
    # Empty string to hold which ascii characters the user wants the function to select from
    chars = ""

    # Empty string which gets passed the characters selected to be in the password
    newPassword = ""

# Checks what ascii characters the user wants to use and adds them to the available characters in the chars variable
    if upper == True:
        chars += string.ascii_uppercase 
    if lower == True:
        chars += string.ascii_lowercase 
    if numbers == True:
        chars += string.digits
    if symbols == True:
        chars += string.punctuation   

# Randomly selects a character from the chars variable and adds it to the newPassword variable. This is done as many times as the user selects
    for i in range(length):
        newPassword += random.choice(chars)

    return newPassword

print('====================================================')
print("=== WELCOME TO CEREALBOXOF'S PASSWORD GENERATOR ====")
print('====================================================')


def getpasswordlength(): 
    while True:
        user_input = input("How long of a password would you like? ")
        if user_input.isdigit():  
            if int(user_input) >= 12 and int(user_input) < 41: 
                return int(user_input) 
            else:
                print("Your password must be between 12 and 40 characters long. ")
        else:
            print(f"{user_input} is not a number. Please try again.") 

length = getpasswordlength() 

def bool_input(type):
    while True:
        user_input = input(type).upper()
        if user_input == "Y":
            return True
        if user_input == "N":
            return False
        else:
            print("You need to enter [Y]es or [N]o ")

upper = bool_input("Include uppercase letters? [Y/N] ")
lower = bool_input("Include lowercase letters? [Y/N] ")
numbers = bool_input("Include numbers? [Y/N] ")
symbols = bool_input("Include symbols? [Y/N] ")

if upper == False and lower == False and numbers == False and symbols == False:
    print("So you don't actually want a password?")
    sys.exit()


print('----------------------------------------------------')
print('Generating password...')
print('----------------------------------------------------')

time.sleep(1.5)

print('====================================================')
print("Your new password is: " + generatePassword(length, upper, lower, numbers, symbols))
print('====================================================')
