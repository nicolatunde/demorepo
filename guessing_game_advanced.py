import random

# Write a program that generates a random number between 1 and 50. 
# Use a while loop to allow the user to guess the number with a maximum of 5 attempts. 
# Provide hints if the guess is too high or too low.


main_loop = True
game_no = 1


while main_loop:
    print(f"*********************STARTING GAME {game_no}*********************")
    attempts = 5
    secret_num = random.randint(1, 50)
    # secret_num = 30

    low, high = 1, 50
    while attempts > 0:
        guess = int(input("Guess the secret number between 1 and 50: "))

        # if guess > 50 or guess < 1:
        # if not(1 <= guess <= 50):
        if guess not in range(1, 51):
            print("Invalid guess. You must guess between 1 and 50")
            continue

        if guess > secret_num:
            high = min(high, guess - 1)
            print(f"You guessed too high. Hint: The number is between {low} and {high}.")
        elif guess < secret_num:
            low = max(low, guess + 1)
            print(f"You guessed too low. Hint: The number is between {low} and {high}")
        else:
            print("Congratulations. You guessed the number correctly!!!")
            break
        attempts -= 1

        if attempts == 0:
            print(f"Sorry, you ran out of attempts. The secret number is {secret_num}")
            break

        print(f"You have {attempts} attempts left.")

    while True:
        keep_playing = input("Do you want to keep playing? yes or no: ").strip().lower()
        if keep_playing == "no":
            main_loop = False
            print("Exiting the program")
            break
        if keep_playing == "yes":
            break
        if keep_playing != "yes":
            print("Enter yes or no.")
            continue
    game_no += 1