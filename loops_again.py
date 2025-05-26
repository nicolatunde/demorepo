# ******************* 6th, May, 2025 ***********************


# Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent:6
# 2 * 2 * 2 * 2 * 2

# base = int(input('Enter the base: ')) # 3
# exponent = int(input('Enter the exponent: '))  # 6
# i = 1
# total = base  
# while i <= exponent:
#     total *= base
#     i += i
# print(total)
    
# print(f'{base} to the power of {exponent} equal to {total}')


#  
# Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no

# acct_bal = float(input('Enter your acct bal: '))




# from time import sleep

# acct_bal = 40_000

# while True:
#     withdrawal_amount = float(input('Enter withdrawal amount: '))
    
#     if withdrawal_amount > acct_bal:
#         print('Insufficient fund')
#         continue
    
#     elif withdrawal_amount <= acct_bal:
#         print('Withdrawing... ')
#         sleep(4)
        
#         acct_bal -= withdrawal_amount
#         print(f"-{withdrawal_amount} amount deducted from your account!\nNew bal: {acct_bal}")

#         question = input('Do you want to make another withdrawal? (yes/no):')
        
#         if question == 'yes':
#             continue
#         elif question == 'no':
#             print('Transaction completed!')
#             break
          
#         else:
#             print('Invalid response. ')
#             break
        
    
    



# 	Write a program that tracks the inventory of items in a store. The user should be able 
# 	to add or remove items and the program should display the current inventory after each
# 	operation. The program stops when the user decides to exit.
# 	The current store inventory is {"eggs’: 40, "fish’: 200, "bread’: 343, "yam’:2}
# 	Sample Input and Output:
# 	Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit



# inventory = {"eggs": 40, "fish": 200, "bread": 343, "yam":2}

# while True:
#     print('Your current inventory is: ', inventory)

#     operation = input('Enter operation (add/remove/exit: )')

#     if operation == 'add':
#         item = input('Enter item: ')
#         qty = int(input('Enter item qty: '))
        
#         if item in inventory:
#             # inventory[item] = inventory[item] + qty 
#             inventory[item] += qty 
#             print(f"{item} added")
#             print('Your current inventory: ', inventory)
#         else:
#             inventory[item] = qty 

    
#     elif operation == 'remove':
#         item = input('Enter item: ')
#         qty = int(input('Enter item qty: '))
        
#         if item in inventory:
#             # inventory[item] = inventory[item] + qty 
#             inventory[item] -= qty 
#             print(f"{item} removed")
#             print('Your current inventory: ', inventory)
#         else:
#             print('Item does not exist')
            
        
#     elif operation == 'exit':
#         print('Thanks for shopping with us! \nExiting...')
#         break





# inventory = {"eggs": 40, "fish": 200, "bread": 343, "yam":2}

# while True:
#     print('Your current inventory is: ', inventory)

#     operation = input('Enter operation (add/remove/exit: )')
    
#     if operation not in ['remove', 'add']:
#         print('Stopping the program')
#         break
    
#     item = input('Enter item: ')
#     qty = int(input('Enter item qty: '))

#     if operation == 'add':
#         if item in inventory:
#             inventory[item] += qty 
#             print(f"{item} added")
#             print('Your current inventory: ', inventory)
#         else:
#             inventory[item] = qty 

    
#     elif operation == 'remove':
#         if item in inventory:
#             # inventory[item] = inventory[item] + qty 
#             inventory[item] -= qty 
#             print(f"{item} removed")
#             print('Your current inventory: ', inventory)
#         else:
#             print('Item does not exist')
            
        
#     elif operation == 'exit':
#         print('Thanks for shopping with us! \nExiting...')
#         break




# How to delay
# from time import sleep



# Guess the number game

import random

# generated_num = random.randint(1, 50)
# print(generated_num)
# user_guess = int(input('Enter the number. Hint: 1-50: ')) # 6

# while generated_num != user_guess:
#     user_guess = int(input('Incorrect guess. Guess again: ')) # 9

# else:
#     print('Correct guess')


import time

generated_num = random.randint(1, 50)
attempts = 5

while True:
    if attempts <= 0:
        print('Sorry no more attempts!')
        break
    
    user_guess = int(input('Enter the number. Hint: 1-50: ')) 

    if user_guess < 1 or user_guess > 50:
        print('Your guess must be between 1 and 50!!')
        continue
        
    if generated_num != user_guess: # 10 + 10
        if (user_guess + 5) < generated_num:
            print('Guess is too low') 
        elif (user_guess - 5) > generated_num:
            print('Guess is too high')
        else:
            print('You almost guessed right')
      
        attempts -= 1
        print('Oh! Sorry, you have', attempts, 'attempts left')
          
        continue
      
    
    else:
        option = input('Correct guess!! \n\nDo you want to play again? yes/no: ')
        if option == 'yes':
            continue
        
        elif option == 'no':
            print('Thank you for playing...')
            print('Exiting...')
            time.sleep(3)
            break
            