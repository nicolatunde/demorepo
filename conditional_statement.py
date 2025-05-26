# name = input("your name:")
# voting_age = int(input("Enter your age"))

# if voting_age >= 18:
#     print(f"congrats, {name}, you are eligible")
# else:
#     print(f"{name}, sorry you aint eligible") 

has_umbrella = False
has_raincoat = True

if has_umbrella == True and has_raincoat == True:
    print("you are well protected from the rain ")
elif has_umbrella == True or has_raincoat == True:
    print("you are protected from the rain ")
else:
    print("you are not protected from the rain")


# mode = input("Enter Mode either manual, automatic or off:").strip().lower()
# if mode == "manual":
#     print("manual mode activated")

# elif mode == "automatic":
#     print("automatic mode activated")

# elif mode == "0ff":
#     print("system is off")
# else:
#     print("its invalid")