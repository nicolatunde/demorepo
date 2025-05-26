# students = ["Tobi", "Dada", "Johnson", "Milly"]

# text = "There are 123 apples and 456 oranges."

# count = 0

# for char in text:
#     if char.isnumeric():
#         count += 1


# phone = "+2349078792471"

# "09089766385"
# "070-442-483-23"

# starts_with_plus = phone.startswith('+')
# after_plus = phone[1:]
# is_actual_number = after_plus.isnumeric()



import re

# Example 1: Simple match
pattern = r"\bword\b"    # He said the word Hello
text = "A word in a wording sentence."
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())  # Match found: word

# Example 2: Find all occurrences
pattern = r"\d+"
text = "There are 123 apples and 456 oranges."
matches = re.findall(pattern, text)
print("Numbers found:", matches)  # Numbers found: ['123', '456']

# Example 3: Replace text
pattern = r"\s+"
text = "This   is a test."
new_text = re.sub(pattern, " ", text)
print("Replaced text:", new_text)  # Replaced text: This is a test.


cars = ["Volvo", "Benz", "Mercedez", "Range"]

''.join(cars)

"Hey            , how is it      going here?"

