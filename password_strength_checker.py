# Scenario: You need to check if a user's password is strong enough.

# Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# Contains at least one special character (e.g., !@#$%^&*()).

# Tip: Check for True or False for each condition of a strong password and chain the boolean results of each of them. If they are all True, the boolean chaining will result to True and result to False if there is at least one False.

# DO NOT USE REGEX.

password = input("enter password:")
charactercount = 0
digit = "0123456789"
digit_count = 0
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
lower_count = 0
uppercase_count = 0
for letter in password:
    if letter in digit:
        digit_count += 1
    elif letter in uppercase:
        uppercase_count += 1
    elif letter in lowercase:
        lower_count += 1
    else:
        charactercount += 1
if all([digit_count,uppercase_count,charactercount,lower_count]) > 0 and len(password) > 8:
    print("very strong password")
else:
    print("weak password")
