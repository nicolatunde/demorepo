# age = int(input('How old are you? '))

# while age < 0: 
#     age = int(input('Invalid age... Please provide valid age: '))
    
# print('Age is valid!!!')


# Write a program that checks if a provided number is a prime number

# number = int(input('Enter the number to confirm if it is prime::: '))

# i = 2

# while i < number - 1:
#     if number % i == 0:
#         print(number, 'is not a prime number')
#         break
#     i += 1
# else:
#     print(number, 'is prime')



# cities = ['ibadan', 'Oyo', 'Ogbomoso', 'Ilorin']


# for i in range(1, 11):
#     print(f'2 * {i} = {2 * i}')
    
# for i in range(1, len(cities)):
#     print(cities[i])

# for city in cities:
#     print(cities[-1], city[0])


# Program that allows you to flexibly provide table number and range and then generate the multiplication table

# n = int(input('enter table: '))
# r = int(input('Provide range: '))

# for i in range(1, r + 1):
#     print(f'{n} * {i} = {i * n}')




# Say, we have a list of games, let's display every single one two times and also with a serial number

# games = ['PES', 'COD', '8 Ball', 'Devil May Cry', 'Assassins Creed', 'PUBG', 'Delta-Force', 'FortNite', 'FIFA']


# # S/N             GAME        
# print(f'S/N\tGAME NAME\n')
# print('*******************')
# for sn, game in enumerate(games, start=1):
#     print(f'{sn}.\t{game}')

# for loop that uses range ()

# print(f'S/N\tGAME NAME\n')
# print('*******************')
# for i in range(0, len(games)):
#     print(f'{i + 1}.\t{games[i]}')
    


# while True:
# # Building a prime number app with a for loop
#     number = int(input('Enter the number to confirm if it is prime::: ')) # 17

#     for i in range(2, number):
#         if number % i == 0:
#             print(number, 'is not prime')
#             break
#     else:
#         print(number, 'is prime')







# Write a program that tells how  many numbers can actually divide a supplied number


# Quickly create a list that contains all odd numbers between 5 and 18
# odd_numbers_list = []

# for i in range(5, 19):
#     if i % 2 != 0:
#         odd_numbers_list.append(i)

# print('Odd numbers: ', odd_numbers_list)


# odd_numbers_list = [i for i in range(5, 19) if i % 2 != 0]

# print('Odd numbers: ', odd_numbers_list)



# games = ['PES', 'COD', '8 Ball', 'Devil May Cry', 'Assassins Creed', 'PUBG', 'Delta-Force', 'FortNite', 'FIFA']

# games_with_length_above_5 = [game for game in games if len(game) > 5]

# print('Games with legnth > 5: ', games_with_length_above_5)

# new_games = []
# for game in games:
#     if len(game)> 5:
#         new_games.append(game)
        
# print('Games with length above 5: ', games_with_length_above_5)







# games = ['PES', 'COD', '8 Ball', 'Devil May Cry', 'Assassins Creed', 'PUBG', 'Delta-Force', 'FortNite', 'FIFA']

# games_with_length_above_5 = [game for game in games if len(game) > 5 else 'UNDEFINED']
# games_with_length_above_5 = [game if len(game) > 5 else 'UNDEFINED' for game in games ]


# new_games = []
# for game in games:
#     if len(game)> 5:
#         new_games.append(game)
#     else:
#         new_games.append('UNDEFINED')
        
# print(new_games)


# let's quickly create a dictionary where the key is a number and the value is the square of that number

# languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "34", "72", "383"]
# newset = {x.upper() for x in languages}
# languages_list = [language.upper() for language in languages]
# print(languages_list)

languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "34", "72", "383"]

new_languages = []

for language in languages:
    if language.isnumeric():
        new_languages.append(int(language))
    # else:
    #     new_languages.append(language)

print('New languages: ', new_languages)



# # Dictionary Comprehension Example:
# languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]

# newdict = {x: len(x) for x in languages}



# numbers = [1, 2, 3, 4, 5]
# Using any() with list comprehension
# numbers = [1, 2, 3, 4, 7]

# print('Any value: :', any(numbers))
# result_any_list = any([x > 5 for x in numbers])


# print(result_any_list)  # Output: False (no element is greater than 5)


# name = input('Enter your name: ').strip()
# age = int(input('Enter your age'))
# school = input('Enter your school: ').strip()

# if name and age and school:
#     print('You have filled all sucessfully')
# elif name and age:
#     print('Also provide your school')


# if all([name, age, school]):
#     print('You have filled all sucessfully')
# elif all([name, age]):
#     print('Also provide your school')
# elif all([school, age]):
#     print('Also provide your name')



# Quickly populate my list with random numbers 30 times.
# import random

# numbers = [random.randint(1, 60) for i in range(30)]


# numbers = [4, 2, 4, 2, 5, 6, 2, 6]

# count = 0

# for number in numbers:
#     if number > 2:
#         count += 1
# print('Total numbers greater than 2 is: ', count)

# for i in range()