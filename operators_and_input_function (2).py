# print(23  + 700)

# Operands
# print("Hello + World")


# num_a = 5
# num_b = 9

# print(num_a % num_b)

# print(7/4)  # 1.75
# print(60 / 13)  # 4.615384615384615
# print(60 // 13)  # 4
# print(60 % 13)  # 8


# print(20 / 13)  # 1.5384615384615385
# print(20 // 13)  # 1
# print(20 % 13)  # 7


# print(13 / 20)  # 0.65
# print(13 // 20)  # 0
# print(13 % 20)  # 13

# print(3 / 9)  # 0.33333
# print(3 // 9)  # 0
# print(3 % 9)  # 1

# print(2 / 5)  # 0.4
# print(2 // 5)  # 0
# print(2 % 5)  # 2


# print(4 / 6)  # 0.7
# print(4 // 6)  # 0
# print(4 % 6) # 7



# print(17 % 3 == 0)


# print(4 ** 2)
# print(10 ** 3)


# print("34" + "21")  # "3421"
# print(34 + 21)  # 55


# print("Akeem" * 3)
# print(3 * "Akeem")

# name = "Nico"

# num1 = 2
# num2 = 6
# # num1 = num1 + num2
# num1 += num2

# print(num1)


# first_num = 7
# second_num = 6
# first_num *= second_num
# first_num /= second_num
# first_num = first_num / second_num
# first_num //= second_num
# first_num = first_num // second_num

# first_num %= second_num
# first_num = first_num % second_num

# first_num = first_num / second_num
# print(first_num)


# print(4 != 4.0)

# print(5.0 <= 5)

# print(70 <= 23)
# print(70 > 23)

# print(7 > 5 and 8 < 7 and 78 > 23)
# print(7 > 5 or 8 < 7)


# print(True and False)
# print(True or False)

# 1. You must have purchased the expensive ticket
# 2. You must have been invited personally to the wedding


# print(not(not False))

# print(not(4 == 5))
# print(4 != 5)

# print(5.0 == 5)
# print(5.0 is 5)


# my_list = ["apple", "banana", "cherry"]
# my_list_2 = ["apple", "banana", "cherry"]


# print(my_list is not my_list_2)
# print(not(my_list is my_list_2))

# interning


# iterables -> list, tuple, string, set, dictionaries

# brand = "Gucci"

# print("H" in "hey")

# my_list = ["apple", "banana", "cherry"]

# print("cherry" not in my_list)

# num = -5
# num = +6


# print(7 - -4)

# print(7 * (9 - 3))
# print(7 * (9 - 3))

# Input function

# name = input("Enter your name: ")

# print(f"Good morning, {name}")

# name = " Winnie "
# print(name.strip())


# from datetime import datetime

# current_year = datetime.today().year

# age = input("How old are you? ")
# birth_year = current_year - int(age)
# print(f"You were born in {birth_year}")


# plural_noun_1 = input("Enter a plural noun: ")
# person_in_room_last_name = input("Enter the last name of a person in the room: ")
# adjective_1 = input("Enter an adjective: ")
# noun_1 = input("Enter a noun: ")
# noun_2 = input("Enter another noun: ")
# part_of_the_body_1 = input("Enter a part of the body: ")
# part_of_the_body_2 = input("Enter another part of the body: ")
# part_of_the_body_3 = input("Enter another part of the body: ")
# noun_3 = input("Enter a noun: ")
# noun_4 = input("Enter another noun: ")
# exclamation = input("Enter an exclamation: ")
# noun_5 = input("Enter a noun: ")
# noun_6 = input("Enter another noun: ")
# noun_7 = input("Enter another noun: ")
# verb_1 = input("Enter a verb: ")
# noun_8 = input("Enter a noun: ")
# adjective_2 = input("Enter an adjective: ")
# noun_9 = input("Enter a noun: ")


# story = f"""A one-act play to be performed by two {plural_noun_1} in this room.
# PATIENT: Thank you so verymuch for seeing me, Doctor {person_in_room_last_name} on such {adjective_1} notice.
# DENTIST: What is your problem, young {noun_1}?
# PATIENT: I have a pain in my upper {noun_2}, which is giving me a severe {part_of_the_body_1} ache.
# DENTIST: Let me take a look. Open your {part_of_the_body_2} wide. Good, now I am going to tap your {part_of_the_body_3} with my {noun_3}.
# PATIENT: Shouldn't you give me a/an {noun_4} killer?
# DENTIST: It's not necessary yet. {exclamation}! I think I see a/an {noun_5} in your upper {noun_6}.
# PATIENT: Are you going to pull my {noun_7} out?
# DENTIST: No, I am going to {verb_1} your tooth and put in a temporary {noun_8}.
# PATIENT: When will I come back for {adjective_2} filling?
# DENTIST: A day after I cash your {noun_9}.
# """


# print(story)


# 1. Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# name = input("Enter your name: ").strip()
# print(f"Hello, {name}!")


# 2. Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”.

# from datetime import datetime
# birth_yr = int(input("Enter your birth year: "))
# current_yr = datetime.today().year
# print(f"You are {current_yr - birth_yr} years old.")



# 3. Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.

# favorite_color = input("Enter your favorite color: ").strip()
# print(f"Your favorite color is {favorite_color}.")


# 4. Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.
# text = input("Enter some text: ").strip()
# text_without_spaces = text.lower().replace(" ", "")
# is_palindrome = text_without_spaces == text_without_spaces[::-1]
# print(f"It is {is_palindrome} that \"{text}\" is a palindrome.")


# 5. Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.

# from getpass import getpass

# password = getpass("Enter your password: ")
# is_valid = len(password) >= 8 and len(password) <= 30
# is_valid = 8 <= len(password) <= 30
# print(f"“It is {is_valid} that the password fulfils the criteria.")


# 6. Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.

# weight = float(input("Enter your weight: "))
# height = float(input("Enter your height: "))
# bmi = weight / (height ** 2)
# bmi = round(bmi, 2)
# print(f"Your BMI is {bmi}")

