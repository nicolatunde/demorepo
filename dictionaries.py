
# mydict = {1: "Tobi", 4: 50}
# # print(mydict[0])
# # print(mydict[int("1")])

# # Create a dictionary that holds a single cart item called "Bournvita" that has a price
# cart_item = {"item_name": "Bournvita", "price": "$500,000"}

# # print("Cart items before update ", cart_item)
# # cart_item["order_id"] = "AB8832"

# # cart_item["order_id"] = "WHITE77"

# # print("Cart items updated to: ", cart_item)

# # animal = {"name": "Dog", "sound" : "Dog", "name" : "Kangaroo"}
# # print(animal["name"])
# # print(animal["sound"])

# # animal_name =  animal["name"]
# # print(f'The name of the animal is: {animal_name}')


# # the del keyword
# # inventory = {
# # "apple": 10, "banana": 5, "orange": 8
# # }

# # print('The data in our inventory is: ', inventory)

# # del inventory["orange"]
# # print('The inventory: ', inventory)



# # inventory = { "apple": 10, "banana": 5, "orange": 8}

# # name, age, course, dept

# # students = [
# #     ["Tobi", 24, "Computer science", "Computerscience"],
# #     ["Winnie", 23, "Computer science", "Computer science"],
# #     ["Nick", 42, "Physics", "Sciences"],
# #     ["Akeem", 16, "Marine Science", "Earth Science"]
# # ]


# # students = [
# #     {"name": "Tobi", "age": 24, "course": "Computer science", "dept": "Computerscience"},
# #     {"name": "Winnie", "age":23,"course":  "Computer science", "dept": "Computer science"},
# #     {"name": "Nick",  "age":42,"course":  "Physics",  "dept": "Sciences"},
# #     {"name": "Akeem", "age": 16, "course": "Marine Science", "dept": "Earth Science"}
# # ]

# # Access Winnie's age
# # print(f"{students[1]["name"]}'s age is: {students[1]["age"]}")
# # # Winnie's age is: 23
# # # Give us Mr. Akeem's dept
# # # The department of the fourth student whose name is "Akeem" is dept. He is 16 years old.
# # print(f"The department of the fourth student whose name is \"{students[3]["name"]}\" is {students[3]["dept"]}. He is {students[3]["age"]} years old.")



# # UPDATE METHOD
# # mydict = {'name': 'Tobi', 'age': 50}


# # # mydict["gender"] = "male"
# # # mydict["complexion"] = "dark"
# # print(mydict)

# # extra_data = {"gender of person": "male", "complexion": "dark"}
# # # mydict.update(extra_data)
# # # print(mydict)


# # mydict = {'name': 'Tobi', 'age': 50}
# # mydict.update(gender="male", complexion="dark", name="Nico")
# # print(mydict)

# # translation = {
# #     "name" : "Oruko",
# #     "girl" : "Obinrin",
# #     "boy" : "Okunrin",
# #     "snake" : "Ejo",
# #     "mother" : "",

# # }


# # print("Fourth translation: ", translation.get("boys", "UNKNOWN"))
# # print("Fourth translation: ", translation.setdefault("boys", "UNKNOWN"))
# # print("Fourth translation: ", translation.setdefault("boy", "UNKNOWN"))

# # print(translation)
# # print('Translation completed!')
# # translation.clear()
# # items, keys, values, pop, popitem
# # print("Updated dictionary: ", list(translation.keys()))

# # print('Values of translations: ', (translation.values()))

# # Check if obirin exists as a "value" in the dictionary
# # print(f"It is {"obinrin" in translation.values()} that obinrin is in the dictionary")

# # print("Items in dict: ", translation.items())
# # print("Items in dict: ", list(translation.items()))

# # _, _, (english, yoruba), *_ = translation.items()
# # print('English word: ', english)
# # print('Yoruba word: ', yoruba)



# # update, pop, popitem


# translation = {
#     "name" : "Oruko",
#     "girl" : "Obinrin",
#     "boy" : "Okunrin",
#     "snake" : "Ejo",
#     "mother" : "IYA",

# }

# print(translation)
# translation["boy"] = ""
# print(translation)


# item = translation.pop('names', "DEFAULT")
# print('Item removed: ', item)
# print('Updated translations: ', translation)


# translation = {
#     "name" : "Oruko",
#     "girl" : "Obinrin",
#     "boy" : "Okunrin",
#     "snake" : "Ejo",
#     "mother" : "IYA",

# }

# english, yoruba = translation.popitem() # last item removed
# print(english, yoruba)

# english, yoruba = translation.popitem() # last removed again
# print(english, yoruba)

# print('Translation: ', translation)
# print('Translation: ', translation)



translation = {
    "name" : "Oruko",
    "girl" : "Obinrin",
    "boy" : "Okunrin",
    "snake" : "Ejo",
    "mother" : "IYA",

}

# translation.pop()
# print('Item removed: ', item)
print('Updated translations: ', translation)
