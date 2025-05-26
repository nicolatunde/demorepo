# Create a dictionary called `student` with keys "name", "age", and "grade", and 
# corresponding values "John", 20, and "A". Access and print the value of "name".
student = {"name": "john", "age": 20}
print(student["name"])

# Create a dictionary called `product` with keys "name", "price", and "stock", and 
# corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
product = {"name": "Laptop", "price": 999.99, "stock": "50"}
product["price"] = 899.99
print(product)

# Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
employee = {"name": "Alice", "position": "Manager"}
employee["salary"] = 50000
print(employee)

# Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".\
inventory = {"apple": 10, "banana": 5, "orange": 8}
# inventory.pop("banana")
print(inventory)
del inventory["banana"]
print(inventory)


# Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.
person = {"anme": "Bob", "age": 25, "city": "New York"}
perons_copy = person.copy()
print(person)

# Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
family = {"child1": {"name": "Nico", "age": 16},
          "child2": {"name": "Winnie", "age": 23},
          "child3": {"name": "Pastore Tobi", "age": 15}
          }
print(f"The age of child2 is {family["child2"]["age"]} years old.")


# Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".
car  = {"brand": "Toyota", "model": "Corolla", "year": 2020}
print(f"The car model is {car["model"]}")
\

# Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
settings = {"volume": 50, "brightness": 85, "language": "English"}
settings["language"] = "Spanish"
print(f"The new language is {settings["language"]}")


# Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
scores = {"match": 90, "science": 85, "english": 88}
scores.pop("science")
print(f"scores after key \"Science\" was removes {scores}")


# Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
menu = {"starter": "Soup", "main_course": "Steak", "dessert": "Ice Cream"}
print(f"it is {"appetizer" in menu} that appetizer is on menu")
# Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
config = {"theme": "dark", "language": "English", "timezone": "UTC"}
config.clear()
print(config)

