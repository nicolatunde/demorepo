# name = "Femi"

# # PEP 8 -> style guide 
# print(name[1:3])


# 17.	Convert a string “James John Kennedy” called “names” to a list using the string 
# .split() method. Store the result in a list called “names_list”
# names = "James John Kennedy"
# names_list = names.split()
# print(names_list)

# print("James John Kennedy".split())

# 18.	You have a list of cities called cities_list containing ['New York', 'Los Angeles', 
# 'Chicago']. Convert this list into a single string where each city is separated by a 
# semicolon and a space. Store the result in a string called cities_string.
# cities_list = ['New York', 'Los Angeles', 'Chicago']
# cities_string = "; ".join(cities_list)
# print(cities_string)

# 19. Create a string variable sentence with the value "the quick brown fox jumps over the 
# lazy dog". Capitalize the first letter of the string and print the result.
# sentence = "the quick brown fox jumps over the lazy dog"
# # capitalized_str = sentence.capitalize()
# sentence = sentence.capitalize()
# print(sentence)
# # print(capitalized_str)
# # print(sentence.capitalize())

# 20. Create a string variable book_title with the value "to kill a mockingbird". Capitalize 
# the first letter of each word and print the result.
# book_title = "to kill a mockingbird"
# book_title = book_title.title()
# print(book_title)

# print(sum([8, 45, 2567]))


# 21. Create a string variable text with the value "hello world". Count the number of 
# occurrences of the letter 'o' and print the result.
# text = "hello world"
# print(text.lower().count("o"))
# print(text.count("o"))


# 22. Create a string variable filename with the value "document.txt". Check if the string 
# starts with "doc" and print the result.
# filename = "document.png"
# print(filename.startswith("doc"))
# print(filename.endswith((".txt", ".doc", ".docx")))
# print(filename.endswith(".txt"))
# print(filename.endswith(".doc"))
# print(filename.endswith(".docx"))

# 23. Create a string variable url with the value "https://www.example.com". Check if the 
# string ends with ".com" and print the result.
# url = "https://www.example.com"
# print(url.endswith(".com"))

# 24. Create a string variable phrase with the value "find the needle in the haystack". Find 
# the position of the word "needle" and print the result.
# phrase = "now find the needle in the haystack"
# print(phrase.find("needle"))

# 25. Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# Result. Bonus point if you can do it with the f-string and concatenation methods also.
# template = "Hello, {}. Welcome to {}."
# name = "Alice"
# place = "Wonderland"
# print(template.format(name, place))

# print(f"Hello, {name}. Welcome to {place}.")

# print("Hello, " + name + ". Welcome to " + place + ".")

# 26. Create a string variable `quote` with the value "To be or not to be". Find the position 
# of the word "not" and print the result.
# quote = "To be or not to be"
# print(quote.find("not"))
# # print(quote.find("Winnie"))
# # print(quote.index("Winnie"))


# 27. Create a string variable word with the value "hello". Check if all characters in the 
# string are lowercase and print the result.
# word = "hello"
# print(word.islower())

# 28. Create a string variable shout with the value "HELLO". Check if all characters in the 
# string are uppercase and print the result.
# shout = "HELLO"
# print(shout.isupper())

# 29. Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# lowercase and print the result.
# mixed_case = "PyThOn"
# print(mixed_case.lower())

# 30. Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# uppercase and print the result.
# mixed_case = "PyThOn"
# print(mixed_case.upper())

# 31. Create a string variable padded_text with the value " hello ". Remove leading whitespace and 
# print the result.
# padded_text = " hello "
# print(padded_text.lstrip())

# 32. Create a string variable padded_text with the value " hello ". Remove trailing whitespace and 
# print the result.
# padded_text = " hello "
# print(padded_text.rstrip())


# 33. Create a string variable padded_text with the value " hello ". Remove both leading and trailing 
# whitespace and print the result.
# padded_text = " hello world "
# print(padded_text.strip(" "))



# 34. Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" 
# and print the result.
# greeting = "Hello, World!"
# print(greeting.replace("world", "Alice"))


# text = "lorem ipsum dolor sit amet "
# # code here
# print(text)  # Lorem ipsum dolor sit amet.




musicians = ["Brymo", "Asa", "Beautiful Nubia", "Wizkid", "Osupa"]
brymo, asa, nubia, wizzy, osupa = musicians

print(brymo)
print(asa)
print(nubia)
print(wizzy)
print(osupa)



# phrase = "star{1} {1} {0}{1}{2}".format("abra", "cad", "abra")
# print(phrase)

num = 9.56755
name = "Nico"
age = 78
print("{0:.3f}".format(num))


# age = 76
# statement = "I am " + str(age) + " years old."
# statement = f"I am {age} years old."
# statement = "I am {}  years old and name".format(age)
# print(statement)


phrase = "star {1} {1} {0}   {1}   {2} jnivjmrfj  iityimtmitg".format("abra", "cad", "abra")
phrase = f" {name} jnivjmrfj  iityimtmitg"
# print = (type(phrase))
print(phrase)
# print(type(phrase))


# padded_text = "   hello world "
# print(padded_text.strip(" "))
# padded_text=padded_text . replace(" ","")
# print(padded_text)


# text = "lorem ipsum dolor sit amet "
# text = text . split()
# print(type(text))
# iya,wura,iyebiye, gfjfjfj, gfhhfhf = text
# print(iya)
# print(wura)
statement = "I am " + str(age) + " years old."
print(statement)
