
# Collect two numbers as input from the user and assign as variables, a and b, write an if 
# statement that prints "a and b are both positive" if both a and b are positive, prints 
# "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# neither is positive.
# a = float(input("Enter Number: "))
# b = float(input("Enter second number: "))
# if a < 0 and b < 0:
#     print("Neither is positive")
# elif a > 0 and b > 0:
#     print("a and b are positive")
# elif a > 0 or b > 0:
#     print("only one is positive")
# # elif a != float(a) and b != float(b):
# #     ("enter a number")
# else:
#     print("invalid")

# Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.
# the_three_number = input("enter 3 numbers seperated by comma: ").strip().replace(" ","").split(',')
# the_three_number = [int(x) for x in the_three_number]
# the_three_number.sort()
# if the_three_number:
#     print("increasing order")
# elif the_three_number == the_three_number.sort(reverse=True):
#     print("strictly decreasing order")
# else:print("notsorted") 

# Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
# palidrome = input("Enter words: ").strip().replace(" ","").lower()
# if palidrome == palidrome[::-1]:
#   print(palidrome,"is a palidome")
# else:
#   print(palidrome,"Not a palidrome")



# You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.

# x = input("Enter value: ")
# y = input("Enter value: ")
# z = input("Enter value: ")
# if x == y == z:
#   print("All same")
# elif x == y or y == z or x == z:
#   print("Two are equall")
# else:
#   print("All different")

# Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".
# angle1 = float(input("enter value: "))
# angle2 = float(input("enter value: "))
# angle3 = float(input("enter value: "))
# if angle1 + angle2 + angle3 == 180 and (angle1 > 0 and angle2 > 0 and angle3 > 0):
#     print("valid triangle")
# else:
#     print("inavlid triangle")

# You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.
# ch = input("enter Letter: ").strip().lower()
# vowel = ("a", "e", "i", "o", "u")
# if ch in vowel:
#    print("its is a vowel")
# else:
#    print("its is a consonant")

# Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".
# colors = set(input("Enter three comma color3: ").strip().split(","))
# primary_colors = {"red", "yellow", "blue"}
# if colors == primary_colors:
#     print("All primary colors")
# else:
#     print("Not all primary colors")

# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".
# mode = input("Enter Mode either manual, automatic or off:").strip().lower()
# if mode == "manual":
#     print("manual mode activated")

# elif mode == "automatic":
#     print("automatic mode activated")

# elif mode == "0ff":
#     print("system is off")
# else:
#     print("its invalid")

# Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".
# message = input("Enter text: ").strip().lower().split()
# if "important" in message or "immediate" in message or "urgent" in message:
#     print("High priority message")
# else:
#    print("Normal message")

# 10.	You have two variables, status1 and status2, provided through user input, each of 
# 	which can be "active", “inactive", or "pending". Write an if statement to print 
# 	"Both active" if both statuses are "active", "One active" if exactly one is "active",
# 	and "None active" if neither is "active".
# status1 = input("enter status: ")
# status2 = input("enter status: ")
# active = "active"
# inactive = "inactive"
# pending = "pending"
# if status1 == active and status2 == active:
#     print("Both active")
# elif status2 == active or status1 == active:
#     print("one active")
# else:
#     print("none active")

#  11. 	Given a string `filename` supplied by the user, write an if statement to check if the
# 	filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# # 	print "Not an image file".
# filename = input("enter file name: ").strip().lower()
# if ".jpg" in filename or ".png" in filename or ".gif" in filename:
#     print("Image file")
# else:
#     print("Not an image")

#  12. 	You have a variable `access_level` provided through user input which can be "admin",
# 	"user", or "guest". Write an if statement that prints "Full access" if access_level is
# 	"admin", "Limited access" if it is "user", and "No access" if it is "guest".
# access_level = input("Enter your position: ").strip().lower()
# if access_level == "admin":
#     print("Full access")
# elif access_level == "guest":
#     print("no access")
# elif access_level == "user":
#     print("Limited access")
# else:
#     print("what on earth are you doing here?")

#  13. 	Given a string `email` collected from the user, write an if statement to check if the
# 	email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
# 	print "Invalid email".
# enter_email = input("enter ur email: ").strip()
# if "@" in enter_email and "." in enter_email:
#     print("valid email")
# else:
#     print("invalid email")
    
#  14. 	You have a variable `day` provided by user input which can be any day of the week 
# 	(e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# 	day is "Saturday" or "Sunday", and "Weekday" if it is any other day.\
# day = input("enter day: ").strip().title()
# week_end = ("Saturday", "Sunday")
# weekday = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# if day in week_end:
#     print("weekend")
# elif day in weekday:
#     print("weekday")
# else:
#     print("enter a valid day of the week")

#  15. 	Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# 	input from the user and prints the greatest number. Use conditional statements
# 	to determine which number is the greatest. Bonus point if you can do it without `else` 
# 	statements.
# enter_number = input("three numbers comma-separated: ").split(",")
# enter_number = [int(x) for x in enter_number]
# # enter_number.sort(reverse=True)
# print(max(enter_number))
# greatest_num = enter_number[0]
# for num in enter_number:
#     if num  >  greatest_num:
#         greatest_num = num
# print(greatest_num)
    






