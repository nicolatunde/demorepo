# Scenario: You need to check if a user's password is strong enough.

# Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# Contains at least one special character (e.g., !@#$%^&*()).

# Tip: Check for True or False for each condition of a strong password and chain the boolean results of each of them. If they are all True, the boolean chaining will result to True and result to False if there is at least one False.

# password = input('Enter a password: ')

# special_chars = '!@#$%^&*()'

# is_long_enough = len(password) >= 8
# has_upper_letters = any(char.isupper() for char in password)
# has_lower_letters = any(char.islower() for char in password)
# has_digit = any(char.isnumeric() for char in password)
# has_special = any(char in special_chars for char in password)

# if all([is_long_enough, has_upper_letters, has_lower_letters, has_digit, has_special]):
#     print('Password is strong')
# else:
#     print('Weak password')










# Generate OTP program

# def generate_otp():
#     sleep(3)
#     generated_otp = randint(1000, 9999)
#     print('Generated OTP!')
#     print(f'OTP is {generated_otp}')
    

# from random import randint
# from time import sleep

# name = input('Enter your name: ')

# option = input('Would you like to get an OTP now (yes/no): ')

# if option == 'yes':
#     print(f'All right, {name}. Generating otp...')
    
#     generate_otp()
    
    
# elif option == 'no':
    
#     print(f'Okay, {name}... See you later. Even though you didnt ask for OTP, here it is ')
#     generate_otp()
    
    








    

# from random import randint
# from time import sleep

# name = input('Enter your name: ')

# option = input('Would you like to get an OTP now (yes/no): ')

# if option == 'yes':
#     print(f'All right, {name}. Generating otp...')
    
#     sleep(3)
#     generated_otp = randint(1000, 9999)
#     print('Generated OTP!')
#     print(f'OTP is {generated_otp}')
    
    
# elif option == 'no':
    
#     print(f'Okay, {name}... See you later. Even though you didnt ask for OTP, here it is ')
#     sleep(3)
#     generated_otp = randint(1000, 9999)
#     print('Generated OTP!')
#     print(f'OTP is {generated_otp}')
    


# def generate_prime(): # arguments and parameters    
#     number = int(input('Enter the number: '))
    
#     for i in range(2, number):
#         if number % i == 0:
#             print(number, 'is not prime number')
#             break
#     else:
#         print(number, 'is prime')

# generate_prime()



# def is_prime(num):
    
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, 'is not prime')
#             break
#     else:
#         print(num, 'is prime.')
    

# is_prime(6, 8)

# is_prime(11)



    # for i in range(2, num):
    #     if num % i == 0:
    #         print(num, 'is not prime')
    #         break
    # else:
    #     print(num, 'is prime.')


# def gen_even_nums(start_num, end_num):
    
#     for i in range(start_num, end_num + 1):
#         if i % 2 == 0:
#             if i == end_num:
#                 print(i)
#             else:
#                 print(i, end=', ')

# gen_even_nums(10,2)

# def gen_even_nums(start_num = 1, end_num = 100):
    
#     for i in range(start_num, end_num + 1):
#         if i % 2 == 0:
#             if i == end_num:
#                 print(i)
#             else:
#                 print(i, end=', ')

# gen_even_nums(end_num=70)


 
# Let's make this function return a value

def gen_even_nums(start_num = 1, end_num = 100):
    list_of_even_nums = []
    
    for i in range(start_num, end_num + 1):
        if i % 2 == 0:
            list_of_even_nums.append(i)
    
    return list_of_even_nums
   

b = gen_even_nums(20)
print(b)

another_even_numbers = gen_even_nums()

print(another_even_numbers)


# print('value returned from gen_even_nums = ', b)

# from random import randint

# random_num = randint(1, 15)

# print('Generated number from randint: ', random_num)



# def add_item(item, my_list=[]):
#     my_list.append(item)
#     return my_list


# mylist = []

# add_item('Tobi', mylist)

# print(mylist)


# # Write a function sum_numbers(a, b) that returns the sum of two numbers.

# def sum_numbers(a, b = 0):
#     c = a + b
#     return c


# something = sum_numbers(5)
