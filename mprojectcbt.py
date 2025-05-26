# total_score = 0
# student_info = {"Tunde": "tubde44", "Akeem": "akeem16", "Tobi": "tobi29"}
# while True:
#     name = input("Enter your name to Login: ")
#     password = input("enter your password: ")
#     if student_info[name] != password:
#         print("wrong credentials ")
#         continue
#     print("login successfull")
#     print("*******WELCOME TO UR CBT QUESTION**********")
#     print(f" student name :{name}")

#     print("""
#     1. What is 2 + 2?
#         a) 3
#         b) 4
#         c) 5
#         d) 6
#     """)
#     option1 = input("enter you answer a-d: ")
#     if option1 == "b":
#       total_score += 1

#     print("""  
#     2. What color is the sky on a clear day?
#         a) Red
#         b) Blue
#         c) Green
#         d) Yellow
    # """)
    # option2 = input("enter you answer a-d: ")
    # if option2 == "b":
    #   total_score += 1

#     print("""  
#     3. How many legs does a spider have?
#         a) 6
#         b) 7
#         c) 8
#         d) 9
#     """)
#     option3 = input("enter you answer a-d: ")
#     if option3 == "c":
#       total_score += 1

#     print("""  
#     4. What sound does a cow make?
#         a) Meow
#         b) Bark
#         c) Moo
#         d) Quack
#     """)
#     option4 = input("enter you answer a-d: ")
#     if option4 == "c":
#       total_score += 1
    

#     print("""  
#     5. What is the opposite of 'hot'?
#         a) Warm
#         b) Cold
#         c) Cool
#         d) Boiling
#     """)
#     option5 = input("enter you answer a-d: ")
#     if option5 == "c":
#       total_score += 1
#     print(f"your total score is {total_score}")
#     break


total_score = 0
student_info = {"Tunde": "tunde44", "Akeem": "akeem16", "Tobi": "tobi29"}
while True:
    name = input("Enter your name to Login: ")
    password = input("enter your password: ")
    if student_info[name] != password:
        print("wrong credentials")
        continue

    print("\n\nlogin successfull\n\n")
    print("*************************************WELCOME TO UR CBT QUESTION**************************************")
    print(f"Student name :{name} \n")
  
    questions_depot = [
        {"question": "1. What is 2 + 2?", "options": "   a) 3 \n   b) 4 \n   c) 5 \n   d) 6", "answer": "b"},
        {"question": "2. What color is the sky on a clear day?", "options": "   a) Red \n   b) Blue \n   c) Green \n   d) Yellow", "answer": "b"},
        {"question": "3. How many legs does a spider have?", "options": "   a) 6 \n   b) 7 \n   c) 8 \n   d) 9", "answer": "c"},
        {"question": "4. What sound does a cow make?", "options": "   a) Meow \n   b) Bark \n   c) Moo \n   d) Quack", "answer": "c"},
        {"question": "5. What is the opposite of 'hot'?", "options": "   a) Warm \n   b) Cold \n   c) Cool \n   d) Boiling", "answer": "c"}
        ]
    for question in questions_depot:
        print(question["question"])
        print(question["options"])
        option = input("Enter your answer a to d: ").strip().lower()
        if option == question["answer"]:
            total_score += 1
    print(f"{name} At the end of the CBT exam, you scored {total_score} points")
    break
        