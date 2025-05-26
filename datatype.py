# String Manipulation

# print("""
#       *********** SENTENCE *********
#       ******************************
#       Hello world this is the first line
#       This is the second line
#       THis is the third line""")


# # Escape characters
# print("Hey, guys.")

# \n
# \r
# \t
# \b
#  \'
# \"

# Concatenate

# print("Tobi" + "Dada")

# fname = "Oluwatobi"
# sname = "Dada"

# Hey, your full name is fullname

# print("Hey, your full name is: ", fname + ' ' + sname)

# fullname = fname + '***' + sname + '.'
# fullname = ""
# print('Fullname is: ', fullname + '...')
# oluwatobi***dada.
# Full name is: oluwatobi***dada....

"""************************ STRING INDEXING ******************"""
institution = "SQI College of ICT" # S is at index 0
# string[index] S C g

# print(institution[2], institution[4], institution[19] )

# "SQI College of ICT"
# I
# Slicing

# len()
# print('Length of ', institution, ' is: ', len(institution) + 5)

# Write a program that stores any sentence inside of a variable called "sentence". Then display the number of characters of that sentence in this format: Chars: 

# "We wrote code today"
sentence = "We are writing our first Python Program today."

# Chars: 12
# print('Chars: ', len(sentence))

# print(sentence[len(sentence) -1 ] )


# print(sentence[-1] + sentence[5] + sentence[-3] + "?")

# print(sentence[len('ball') - 2] + sentence[-4] + " yellow card "[5] + "yellow card"[-1][-1]+ sentence[-1])

# 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 20





# Create two string variables: first_name with value "John" and last_name with value 
# "Smith". Concatenate them together with a space in between and print the result.

# Given the string word = "Python", print the first character.


# Given the strings part1 = "Data" and part2 = "Science", concatenate them to form "DataScience" and print the result.
# part1= "Data"
# part2 = "Science"
# print(part1 + part2)

# Given the string phrase = "Welcome", print the last character using negative indexing.
# phrase = "Welcome"
# print(phrase[len(phrase)-2])



# Given the strings str_1 = "Good" and str_2 = "Morning", concatenate them with a space in between to form "Good Morning" and print the result.
# str_1 = "Good" 
str_2 = "Morning"

# print(str_1 + ' ' + str_2)
# print(str_1, str_2)

# Given the string text = "Concatenate", print the character at index 5.
# text = "Concatenate"
# print("The character at index 5 is: ", text[5])

# print("The character at index 5 is: ", text[len(str_2)-1] + 'square.')


# Create three string variables: city = "New", space = " ", and country = "York". Concatenate them to form "New York" and print the result.

# city = "New" 
# space = " "
# country = "York"
# print(city + space + country)

# print(city, space, country, sep='')

# Given the string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", print the 10th character.
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(alphabet[9])


# Given the strings a = "Super" and b = "Hero", concatenate them to form "SuperHero" and print the result.
# a = "Super"  
# b = "Hero"


# .ea?


# 14, 16, 17, 20

# Given the string universe = "MilkyWay", print the third character from the end using 
# negative indexing.
# universe = "MilkyWay"
# print(universe[-3][0])


# String Immutability
# word = "Hello"
# word[3] = "J"
word = "Hello World"

# string[start_index : end_index : step]
# print(word[0:4])

print(word[6:11:4])

# string[start_index : end_index : step]
# institution = "SQI College of ICT"
# name = "Seun"
# print(institution[0:12:2]) # SIC


text = "Hello, World!"
# print(text[:5])   
# print(text[7:])   
# print(text[7::2])   
# print(text[0:len(text)-4])
# print(text[0:-4])

# print(text[:-3:-2]) #hlo o
# print(text[::-2])
# print(text[::-1])
# text = "Hello, World!"
# print(text[::-1][::-1])

# String Interpolation















