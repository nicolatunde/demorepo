import random

# Write a program that generates a random number between 1 and 50. 
# Use a while loop to allow the user to guess the number with a maximum of 5 attempts. 
# Provide hints if the guess is too high or too low.


attempts = 5
secret_num = random.randint(1, 50)
while attempts > 0:
    guess = int(input("Guess the secret number between 1 and 50: "))

    # if guess > 50 or guess < 1:
    # if not(1 <= guess <= 50):
    if guess not in range(1, 51):
        print("Invalid guess. You must guess between 1 and 50")
        continue

    if guess > secret_num:
        print(f"You guessed too high.")
    elif guess < secret_num:
        print(f"You guessed too low.")
    else:
        print("Congratulations. You guessed the number correctly!!!")
        break
    attempts -= 1

    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The secret number is {secret_num}")
        break

    print(f"You have {attempts} attempts left.")

