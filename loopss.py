# i = 1
# while i < 100:
#     i += 1
#     print(f"{i}.Nico")

# i = 10
# while i <= 70:
#     if i % 5 ==0 and i % 3 == 0:
#         print(i)
#     i += 1

# i = 1
# holder = ""
# while i <= 50:
#     if i < 50:
#         holder += f"{i}, "
#     else: 
#         holder += f"{i}"
#     i += 1
# print(holder)

# import getpass
# password = getpass.getpass("Enter password: ")
# sttored_password = "nicoNico"
# if password == sttored_password:
#     print("password is correct")
# else:
#     print("incorrect password")

# i = 1
# j = 2
# containersu = ""
# while i <= 12:
#     print (f"{j} times {i} = {j * i} " )
#     i += 1
    # number += 1
# print(containersu)



# animal = {"name": "Dog", "sound" : "house", "names" : "Kangaroo",}
# print("Dog" in animal["name"])



# members_logindetail = {"dom": "dum"}
# print("enter user name and password to signup")
# entered_name = input("enter name: ")
# if entered_name in members_logindetail:
#    while entered_name in members_logindetail:
#     print("username already exists")
#     entered_name = input("enter name: ")
# entered_password = input("enter password: ")
# if len(entered_password) < 5:
#     print("minimum of 5 character") 
#     while len(entered_password) < 5:
#       entered_password = input("re-nter password: ")
# members_logindetail[entered_name] = entered_password

# print("sign in ")
# login_entered_user_name = input("user name: ")
# login_entered_password = input("password: ")

# if (login_entered_user_name in members_logindetail) and (login_entered_password == members_logindetail[login_entered_user_name]):
#    print("login successfull")
# else:
#     print("wrong password or username")



i = 1
j = int(input("enter number"))
while i <= 12:
    print (f"{j} X {i} = {j * i} " )
    i += 1


# for item in [1, 2, 3]:
#     print(item)

# cities = ["New York", "Paris", "Tokyo", "Sydney", "Cairo"]
# for city in cities:
#     print(f"City: {city}")


# items = ("guitar", "keyboard", "drums", "microphone", "amp")
# for item in items:
#     print(f"Item: {item}")


# capitals = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'Australia': 'Canberra', 'Egypt': 'Cairo'}
# for country in capitals:
#     print(f"Country: {country}")


# for capital in capitals.values():
#     print(f"Capital: {capital}")

# for country, capital in capitals.items():
#     print(f"Country: {country}, Capital: {capital}")

# books = {"1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby Dick", "Pride and Prejudice"}
# for book in books:
#     print(f"Book: {book}")


# # Exit the loop when x is "stop":
# actions = ["run", "jump", "stop", "walk"]
# for x in actions:
#   print(x)
#   if x == "stop":
#     break

# Exit the loop when x is "stop", but this time the break comes before the print:
# actions = ["run", "jump", "stop", "walk"]
# for x in actions:
#   if x == "stop":
#     break
#   print(x)

# tasks = ["start", "process", "skip", "finish"]
# for x in tasks:
#   if x == "skip":
#     continue
#   print(x)

# Using the range() function:

# for x in range(6):
#   print(x)

# for x in range(1, 6):
#   print(x)
# x in range(10)


# for x in range(2, 30, 3):
#   print(x)


# fruits = {'apple', 'banana', 'cherry'}
# for index, fruit in enumerate(fruits, start=0):
#     print(f"{index}: {fruit}")


# fruits = ['apple', 'banana', 'cherry']
# for index in range(len(fruits)):
#     print(f"{index + 1}: {fruits[index]}")

# for x in range(2, 15):
#   print(x)
# else:
#   print("Finally finished!")


# for x in range(20):
#   if x == 21: break
# else:
#   print("Finally finished!")

