# How to count number (forward and in reverse)
# How to count while adding steps
# While statement combined with if statement
# While True
# Multiplication table.

# Number 1 in slide 31
# How to loop through list, string and others using


# For loop
# While loop


# while boolean_expr:
#       # body

# Infinite loop

# name = input('Enter your name: ')
# number_of_times = int(input('How many times should I display it: ')) 

# i = 1
# while i <= number_of_times:
#     print(f'{i}. {name}')
#     i += 1

# Write a program to print even numbers between 0 and 200 using a while loop

# i = 0
# while i < 200:
#     print(i)
#     i += 2

# Write a program to print even numbers between 3 and 251 using a while loop
# i = 3
# while i < 15: # 3, 4
#     if i % 2 == 0:
#         print(i)
#     i += 1
 
# Quickly talk about doing decreasing order of loop

# i = 100
# while i > 0:
#     i -= 4
#     print(i)
 
# i = 4
# mylist = "Balablu"
# print(mylist[i])  # k
# i += 2

# print(mylist[i]) # s



# student = "Tobi Dada"

# while i < len(student)//2:
#     print(student[i] * 3 , end='')
#     i += 1
    


    
# Get all the numbers between 10 and 70 that are mutiples of both 3 AND 5
#  Use a while loop to print your name 100 times.

# The variables commonly used by convention in loops are i, j, k


# While True
# Multiplication table.

# Number 1 in slide 31
# How to loop through list, string and others using
# cities = ['Lagos', 'Abuja', 'Port Harcourt', 'Ibadan', 'Enugu']
# i = 0

# while i <= len(cities):
#     print(cities[i][0])
#     i += 1




# i = 2

# while i <= 14:
#     print('Py')
#     # if i == 7:
#     #     continue
    
#     i += 1
#     break
    
# else:
#     print('Okay, loop completed successfully')



# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)



# for i in range(1, 1000, 2):
#     print(i)


# cities = {'city1': 'Abuja', 'city2': "Lagos", 'city3': 'onitsha'}

# for city in cities.items():
#     print(city)
# for-each

# for ch in 'aeiou':
#     print(ch)


# tasks = ["start", "process", "skip", "finish"]
# for x in tasks:
#   if x == "skip":
#     break
#   print(x)


fruits = ['apple', 'banana', 'cherry']

# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}. {fruit}")

# for i in range(0, len(fruits)):
#     print(f"{i + 1}. {fruits[i]}")

# generator function

# mylist = []

# for i in range(1001):
#     mylist.append(i)

# print(mylist)


# mylist = []

# for i in range(1001):
#     mylist.append(i)

# print(mylist)

# Let's have a list of even numbers between 300 and 580

# Using the range() function to quickly generate a list of numbers in a sequence
# print(list(range(300, 581, 2)))


# for i in range(10):
#     print('Hi')
#     pass

# for i in range(10): # 0, 1
#     for j in range(5): # 0, 1
#         for k in range(16): 0, 15, 0, 15
            

# cities = [['city1', 'city2', 'city3', 'city4', ['city5', 'city6']], ['badan', 'Ogbomoso', 'Osun'],
#           ['Ilorin', 'Ilesha', 'Kwara']]

# # # 
# for city in cities:
#     for city_item in city:
#         if isinstance(city_item, list):
#             for inner_city_item in city_item:
#                 print(inner_city_item)
#         else:
#             print(city_item)
    
    

# cities = [['city1', 'city2', 'city3', 'city4', ['city5', 'city6']], ['badan', 'Ogbomoso', 'Osun'],
#           ['Ilorin', 'Ilesha', 'Kwara']]

# normal_list = []
# # # 
# for city in cities:
#     for city_item in city:
#         if isinstance(city_item, list):
#             for inner_city_item in city_item:
#                 normal_list.append(inner_city_item)
#         else:
#             normal_list.append(city_item)
    
# print(normal_list)



# Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent:6
# 2 * 2 * 2 * 2 * 2

base = int(input('Enter the base: ')) # 3
exponent = int(input('Enter the exponent: '))  # 6
i = 1
total = base  
while i <= exponent:
    total *= base
    i += i
print(total)

print(f'{base} to the power of {exponent} equal to {total}')


#  
