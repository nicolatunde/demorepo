import re
import sqlite3
import hashlib

from getpass import getpass

conn = sqlite3.connect('instagram.db')
cursor = conn.cursor()

def main():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        password TEXT NOT NULL
        )
    """)


    def sign_up():
        while True:
            first_name = input("Enter your first name: ").strip()

            if not first_name:
                print("First name cannot be blank")
                continue
            break


        while True:
            last_name = input("Enter your last name: ").strip()
            if not last_name:
                print("Last name field cannot be blank")
                continue
            break


        while True:
            username = input("Enter your username: ").strip()
            if not username:
                print("Username field cannot be blank")
                continue
            break

            
        while True:
            email = input("Enter your email address: ").strip()
            if not email:
                print("Email field cannot be blank")
                continue

            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            match = re.match(pattern, email)
            if not match:
                print("Email address is invalid")
                continue

            break

        while True:
            password = getpass("Enter your password: ").strip()
            if not password:
                print("Password field cannot be blank")
                continue

            confirm_password = getpass("Confirm your password: ").strip()
            if not confirm_password:
                print("Confirm Password field cannot be blank")
                continue

            if password != confirm_password:
                print("Passwords don't match")
                continue
            break

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            cursor.execute("INSERT INTO users (first_name, last_name, username, email, password) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, username, email, hashed_password))
        except sqlite3.IntegrityError as e:
            print("Integrity Error: ", e)
        else:
            print("Account created successfully 😁")
            conn.commit()
            log_in()


    def log_in():
        print("\n*************************LOG IN*******************************")
        username = input("Enter your username: ").strip()
        password = getpass("Enter your password: ").strip()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        user = cursor.execute("SELECT id, first_name FROM users WHERE username = ? AND password = ?", (username, hashed_password)).fetchone()
        if user is None:
            print("Incorrect credentials")
        else:
            print("Log In Successful 😁")
            instagram_menu(user)
            

    def instagram_menu(user):
        id, first_name = user
        print(f"Welcome, {first_name}")
        menu = """
        *************************INSTAGRAM*******************************
        1. For You Page
        2. Reels
        3. Profile
        4. Messages
        5. Return to Main Menu
        """

        while True:
            print(menu)
            choice = input("Choose an option from the menu above: ").strip()
            if choice == "1":
                print("For You Page")
            elif choice == "2":
                print("Reels")
            elif choice == "3":
                print("Your Profile")
            elif choice == "4":
                print("Inbox")
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
                continue




    menu = """
    *************************HOME*******************************
    1. Sign Up
    2. Log In
    3. Quit
    """

    while True:
        print(menu)
        choice = input("Choose an option from the menu above: ").strip()
        if choice == "1":
            sign_up()
        elif choice == "2":
            log_in()
        elif choice == "3":
            print("Good bye 👋")
            break
        else:
            print("Invalid choice")
            continue
    


try:
    main()
except Exception as e:
    print(f"Oops! something went wrong: {e}")
finally:
    conn.close()