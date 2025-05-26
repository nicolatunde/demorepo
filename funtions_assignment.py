# # Write a function sum_numbers(a, b) that returns the sum of two numbers.
# def sum_of_two_numbers(num1 = 1,num2 = 1):
# #     sum = num1 + num2
# #     print("The sum of the two numbers is ",sum)
# # sum_of_two_numbers(1,7)

# # # Write a function is_even(n) that returns True if n is even and False if n is odd.

# # def is_even(i):
# #     if i % 2 == 0:
# #         print(True) 
# #     else:
# #         print(False)
# # is_even(5)


# # # Write a function is_prime(n) that returns True if n is a prime number and False otherwise.
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True




# def list_prime_number():
#     n = int(input("enter value of n: "))
#     list_prime_num_upto_num = []
#     for i in range(2, n+1):
#         if is_prime(i):
#             print("true")
#             list_prime_num_upto_num.append(i)
#     return list_prime_num_upto_num
# print(list_prime_number())

# # Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.
# # def is_prime(n = 100):
# #     prime_num_upto_num = ""
    
# #     for i in range(2,n):
# #         if n % i == 0:
# #             return False
# #     return True

# # n = int(input("enter a number: "))
# # result = is_prime(n)
# # print(result)

# # Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.
# def lesser_of_two_evens(a, b):
#     greater_0r_lesser = ""
#     if all([a % 2, b % 2]) == 0:
#         lesser_num = a
#         if b < lesser_num:
#             lesser_num = b
#         greater_0r_lesser += f"The lesser number is : {lesser_num}"
#     elif any([a % 2,b % 2])  != 0:
#         greatest_num = a
#         if b > greatest_num:
#             greatest_num = b
#         greater_0r_lesser += f"The greatest num is:, {greatest_num}"
#     return greater_0r_lesser

# result = lesser_of_two_evens(2, 14)
# print(result)

# Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
#  is_alliteration(‘Levelheaded llama’) —> True
# # is_alliteration(‘Crazy Kangaroo’) –> False

# def is_alliteration(a = "love you"):
#     a = a.strip().lower().split(" ")
#     item1,item2 = a
#     if item1[0] == item2[0]:
#         print(True)
#     else:
#         print(False)

# is_alliteration("Love Letter")

# Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.

# def old_macdonald(name = "macdonald"):
#     name = list(name)
#     name[0] = name[0].capitalize()
#     name[3] = name[3].capitalize()
#     name = "".join(name)
#     print(name)
# old_macdonald("house")
    
# Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False

# def spy_game(spy_game = [1, 2, 4, 0, 0, 7, 8]):
#     counter = ""
#     spy_checker = "007"
#     for char in spy_game:
#         if char == 0 or char == 0 or char == 7:
#             counter += str(char)
#     if spy_checker == counter:
#       return True
#     else:
#        return False
      
    
# spy_game([1, 7, 2, 0, 4, 5, 0])
        


# Write a function vol(radius) that computes the volume of a sphere given its radius.
# Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).
# Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.
# Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.



def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def divission(a,b):
    return a/b

def multiplication(a,b):
     return a*b

# print("""
# *******************Welcome to the Simple Calculator*******************************
# Select operation:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
#       """)
# while True:
#   option = input("which operation do u want to perform: ")
#   if option == "5":
#       print("exiting*************")
#       break
#   number1 = int(input("enter a number: "))
#   number2 = int(input("enter a number: "))
#   if option == "1":
#       addition(number1,number2)
#       print(f"{number1} + {number2} = {addition(number1,number2)}")
#   elif option == "2":
#       print(f"{number1} - {number2} = {subtraction(number1,number2)}")
#   elif option == "3":
#       print(f"{number1} x {number2} = {multiplication(number1,number2)}")
#   elif option == "4":
#       print(f"{number1} / {number2} = {divission(number1,number2)}")

# Write a function vol(radius) that computes the volume of a sphere given its radius.
  

# def vol(r):
#     volume = (4/3) * 3.14159 * (r**3)
#     volume = round(volume,2)
#     return volume
# print(vol(20))
  

