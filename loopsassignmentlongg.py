# Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)

# numbers = input("enter a digit")
# sum_of_digit = 0
# sum_in_string_format = ""
# i = 0
# for number in numbers:
#     sum_of_digit += int(number)
#     if i > 0:
#      sum_in_string_format +=f"+{number}"
#     else:
#        sum_in_string_format += number
#     i += 1
# print(f"{sum_of_digit} ({sum_in_string_format})")    


# Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7

# text = input("enter a sentence:").lower().replace(" ","")
# vowels = "aeiou"
# vowel_count = 0
# consonants_count = 0
# consonants = "bcdfghjklmnpqrstvwxyz"
# character_counts = 0
# for letter in text:
#    if letter in vowels:
#       vowel_count += 1
#    elif letter in consonants:
#       consonants_count += 1
#    else:
#       character_counts += 1
# print(f"vowels: {vowel_count} consonants: {consonants_count} characters: {character_counts}")
      
   
# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60

# number = int(input("Enter a number: "))
# for x in range(1,13):
#     print(f"{number} x {x} = {number * x}")

# Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"

# text = input("enter at text:")
# # for i in range(10,1,-1):
# #     print(i)
# reversed_form = ""
# for i in range(len(text)-1, -1, -1):
#       reversed_form += text[i]
# print(reversed_form)

# output = ""
# for i in range(len(text)-1, -1,-1):
#     output += text[i]
# print(output)

# text = input("enter text: ")
# output = ""
# i = 0
# j = -1

# while i < len(text):
#     output += f"{text[j]}"
#     i += 1
#     j -= 1
# print(output)


# Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# numbers = input("enter comma seperated numbers").strip().split(",")
# new_list = []
# for number in numbers:
#     number = int(number)
#     if number not in new_list:
#         new_list.append(number)
    
# print(new_list)

# for number in numbers:
#     if number.isnumeric():
#        if int(number) % 2 == 0:
#          print(number)
         


#  6.	Write a program that takes an integer input n from the user and prints the first 
# 	n numbers in the Fibonacci sequence. Example:
# 	Input: 10
# 	Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# fibonacci_sequence = [0, 1,]
# # i = 0
# number = int(input("enter a number: "))

# while i < number-2:
#     fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
#     i += 1
# print(fibonacci_sequence)

# for x in range(2,number):
#     fibonacci_sequence.append(fibonacci_sequence[x-1] + fibonacci_sequence[x-2])
# print(fibonacci_sequence)


#  7. 	Collect a list of numbers from the user (entered as comma-separated values) and use a 
# 	loop to find and print the largest number in the list. Don’t use the built-in max 
# 	function or anything similar.
# 	Input: "10, 20, 5, 15"
# # 	Output: 20

# numbers = input("enter comma seperated numbers").strip().split(",")
# numbers = "2,3,4,5,6".strip().split(",")
# int_list_version = []
# for number in numbers:
#     int_list_version.append(int(number))
# greatest_num = int_list_version[0]
# for number in int_list_version:
#     if number > greatest_num:
#      greatest_num = number
# print(greatest_num)

#  8. 	Write a program that takes an integer n from the user and calculates the sum of all 
# 	even numbers from 1 to n. Print the sum.
# 	Input: 10
# 	Output: 30 (2 + 4 + 6 + 8 + 10)

# numbers = int(input("enter a number"))
# sum_of_even_num = 0
# each_even_numbers = ""
# for number in  range(1,numbers+1):
#      if number % 2 == 0:
#       sum_of_even_num += number
#       if number > 2:
#        each_even_numbers += f"+{str(number)}"
#       else:
#          each_even_numbers += f"{str(number)}"
# print(f"{sum_of_even_num} ({each_even_numbers})")


#  9. 	Collect a string from the user and use a loop to count the frequency of each character 
# 	in the string. Print each character along with its frequency. Example:
# 	Input: "hello"
# 	Output:
# h: 1
# e: 1
# l: 2
# o: 1

         
