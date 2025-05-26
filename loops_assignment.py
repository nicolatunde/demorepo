# Write a program that uses a while loop to print numbers from 1 to 10.

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop.

# n = int(input("Enter a number: "))
# i = 1
# sum_all = 0
# while i <= n:
#     sum_all += n
#     n += -1
# print(sum_all)


# Write a program that generateser between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. a random numb



# Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.
# password = "secret"
# entered_password = input("Enter password: ")
# while entered_password != password:
#     print("incorrect password")
#     entered_password = input("Renter password: ")
    
# else:
#     print("login successful")
    
# Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.

# countdown_from = int(input("start countdown from: "))
# i = 0
# while i <= countdown_from:
#     print(countdown_from)
#     countdown_from -= 1

# Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# n = int(input("Enter number: "))
# while n >= 1:
#     if n % 2 == 0:
#         print(n)
#     n -= 1

# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1



# Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625

# base = int(input('Enter the base: ')) # 3
# exponent = int(input('Enter the exponent: '))  # 6
# i = 1
# total = base  
# while i <= exponent:
#     total *= base
#     i += i
# print(total)

# print(f'{base} to the power of {exponent} equal to {total}')



# Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.
# enter_text = input("enter text: ").lower()
# vowel = "aeiou"
# count = 0
# i = 0
# while i < len(enter_text):
#     if enter_text[i] in vowel:
#         count += 1
#     i += 1
# print(count)    

# Write a program that takes a string input from the user and uses a while loop to reverse the string.
# text = input("enter text: ")
# i = 0
# j = -1
# container = ""
# while i < len(text):
#     container += text[j]
#     i += 1
#     j -= 1
# print(container)


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
# Final balance: 350

# entered_balance = int(input("enter your balance: "))
# entered_withdrawal_amount = int(input("enter withdrawal amount: "))
# while entered_withdrawal_amount > entered_balance:
#     print("insufficient fund")
#     entered_withdrawal_amount = int(input("enter valid  withdrawal amount: "))
# remaining_banace = entered_balance - entered_withdrawal_amount
# print("remaining balance is :",remaining_banace)
# continue_transaction = True
# while continue_transaction:
#     more_withdrawal = input("do you want to make more withdrawal: ").lower()
#     if more_withdrawal == "yes":
#         entered_withdrawal_amountbb = int(input("enter withdrawal amount: "))
#         remaining_banace -= entered_withdrawal_amountbb
#         print("final balance is : ",remaining_banace)
#     elif more_withdrawal == "no":
#         print("transaction complete thank you")
#         break





# Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48

# entered_item_price = float(input("enter item price: "))
# total_cost = entered_item_price
# while True:
#     enter_another_items = (input("enter another items? ")).lower()
#     if enter_another_items == "yes":
#         entered_item_price = float(input("enter item price: "))
#         total_cost += entered_item_price
#     elif enter_another_items == "no":
#         print("order complete")
#         break
#     else:
#         print("enter a valid response")
        
# print(f"Total cost is: ${total_cost}")




# Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.

# print("Password must be at least 8 characters long and have a maximum of 25 characters.")
# entered_password = input("enter password: ")
# while len(entered_password) < 8 or len(entered_password) > 25:
#     print("invalid password")
#     entered_password = input("enter password: ")
# else:print("valid password")

# while True:
#     print("Password must be at least 8 characters long and have a maximum of 25 characters.")
#     entered_password = input("enter password: ")
#     if len(entered_password) < 8 or len(entered_password) > 25:
#      print("invalid password")
     
#     else:
#        print("correct password")
#        break




# # # 4.	Write a program that asks for the user's age and keeps prompting them until they 
# # 	enter a valid age (greater than or equal to 0).
# # 	Sample Input and Output:
# # 	Enter your age: -5
# # 	Invalid age. Please enter a valid age.
# # 	Enter your age: 25
# # 	Age accepted.

# while True:
#     age = int(input("how old are you ? "))
#     if age < 0:
#       print("inavalid age.Please enter a valid age")
#       continue  

#     print(f"{age} is accepted")
#     break

# #  5. 	Write a program that tracks the inventory of items in a store. The user should be able 
# # 	to add or remove items and the program should display the current inventory after each
# # 	operation. The program stops when the user decides to exit.
# # 	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# # 	Sample Input and Output:
# # 	Enter operation (add/remove/exit): add
# # Enter item: eggs
# # Enter quantity: 10 
# # Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# # Enter operation (add/remove/exit): remove
# # Enter item: fish
# # Enter quantity: 50
# # Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# # # Enter operation (add/remove/exit): exit
# store_inventory = {"eggs": 40, "fish": 200, "bread": 343, "yam":2}
# enter_items = input("enter item:").strip().lower()
# while enter_items not in store_inventory:
#     print("enter a valid item") 
#     enter_items = input("enter item:")
# enter_quantity = int(input("enter quantity"))
# store_inventory[enter_items] = store_inventory[enter_items] + enter_quantity
# print(store_inventory)
# cont_operation = True
# while cont_operation:
#     entered_operation = input("remove,add,or exit ").strip().lower()
#     if entered_operation == "add":
#         enter_items = input("enter item:").strip().lower()
#         enter_quantity = int(input("enter quantity "))
#         store_inventory[enter_items] = store_inventory[enter_items] + enter_quantity
#         print(store_inventory)
#     elif entered_operation == "remove":
#          enter_items = input("enter item: ")
#          enter_quantity = int(input("enter quantity "))
#          store_inventory[enter_items] = store_inventory[enter_items] - enter_quantity
#          print(store_inventory)
#     elif entered_operation == "exit":
#         print("transaction complete")
#         break
#     else:
#         print("enter a valuable response")

# print("final list is" ,store_inventory)


        
    