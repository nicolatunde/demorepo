import re
import sqlite3
from random import randint
import hashlib
from getpass import getpass
from time import sleep
import sys
from datetime import datetime

conn = sqlite3.connect('bankingapp.db')
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        account_balance INTEGERS NOT NULL,
        account_number TEXT NOT NULL
           )
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        amount REAL NOT NULL,
        type TEXT NOT NULL,
        sender TEXT,
        balance REAL NOT NULL,
        recipient TEXT,
        user_id INT NOT NULL,
        description TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
           )
""")



def create_account():
    while True:
        first_name = input("Enter your first name: ").strip().lower()
        if not first_name:
               print("field cannot be left blank")
               continue
        pattern = r"^[a-zA-Z]+$"
        match = re.match(pattern,first_name)
        if match:
            break
        print("enter only alphabet")
        continue

    while True:
        sure_name = input("Enter your surename :").strip().title()
        if not sure_name:
               print("surename field cannot be left blank")
               continue
        pattern =  r"^[a-zA-Z]+$"
        match = re.match(pattern,sure_name)
        if match:
            break
        print("enter only alphabet")
        continue
    full_name = ((sure_name).title() + " " + (first_name).title())
    
    while True:
        user_name = input("Enter your prefered username :").strip()
        if not user_name:
               print("user field cannot be left blank")
               continue

        pattern = r'^(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]{3,20}(?<![_.])$'
        
        match = re.match(pattern,user_name)

        if match:
            user = cursor.execute(f"SELECT * FROM users WHERE username = ?",(user_name,)).fetchone()
            conn.commit()
            if user is None:
                break
            print(f"{user_name} user already exist enter another username")
            continue
        else:
            print("username not valid please enter a another username")
            continue
        
    
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
        user_check = cursor.execute(f"SELECT * FROM users WHERE email = ?",(email,)).fetchone()
        conn.commit()
        if user_check is None:
            break
        print("email already exist enter another email")

    while True:
        print("create password below lenght of password not less than 8 with Upper case,lower case,number,and special character.")
        password = getpass("create a secure password: ").strip()
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9])[\s\S]{6,12}$'
        match = re.match(pattern, password)
        if not match:
            print("enter a strong password")
            continue
        confirm_password = getpass("confirm your password :").strip()
        if confirm_password != password:
            print("password doesnt match")
            continue
        break
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

           
    while True:
        try:
            initial_deposite = float(input("enter your initial deposit #2000.00 minimum: #"))
        except ValueError as e:
            print("enter a valid input")
            continue
        except Exception  :
            print("invalid input")
            continue    
        if initial_deposite < 2000:
            print("opps the lowest initial deposit is #2000.00 re-enter")
            continue
        break
      


    while True:
        account_number = str(randint(1102001000,1112000000))
        Account_checker = cursor.execute("SELECT * FROM users WHERE account_number = ?",(account_number,)).fetchone()
        conn.commit()

        if Account_checker is None:
            break
        continue


    try:
        cursor.execute('''
            INSERT INTO users ('full_name', 'username', 'email', 'password', 'account_balance', 'account_number') values (?, ?, ?, ?, ?, ?)
        ''',(full_name, user_name, email, hashed_password, initial_deposite, account_number))
        conn.commit() 

        user_id = cursor.execute("SELECT id, full_name FROM users WHERE username = ?",(user_name,)).fetchone()
        conn.commit()
        id,name = user_id
        cursor.execute('''INSERT  INTO transactions ('balance', 'amount', 'type', 'user_id') VALUES (?, ?, ?, ?) ''',(initial_deposite, initial_deposite, 'initial deposite', id,))
        conn.commit()

    except sqlite3.IntegrityError as e:
        print("am error occured ",e)
    except Exception as a:
        print("am error occured ",e)
        
 
    loading("creating account")


    print(f'''congratulation {first_name} account successfully created
          Account Name:  {full_name}
          Account number: {account_number}
          email: {email}
          current balance: #{initial_deposite}
          ''')
    loading("redirecting to login page")
    login()
    
    


def login():
    counter = 3
    while counter > 0:
        if counter <= 2:
            print("you have ",counter,"attempt left")  
        print("*****Enter your details to login*******")
        while True:
            user_name = input("Enter your username: ").strip()
            if not user_name:
                ("field cannot be left empty")
                continue
            break
        while True:
            password = getpass("Enter your password: ").strip()
            if not password:
                ("field cannot be left empty")
                continue
            break
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = cursor.execute('SELECT id, full_name FROM users WHERE username = ? and password = ?', (user_name, (hashed_password),)).fetchone()
    
        if user is None:
            print("wrong password or username")
            counter -= 1
            continue
        else:
            id, name = user
            print("login successful")
            loading("loading your dashboard please wait")
            dashboard(id,name)
            break 



def dashboard(id,name,):
        print(f"\n HLLO  {name}!!!!!!!!! Wellcome to your dashboard")
        menu = f'''
        which operation would like to perform choose option bellow 
        1. Deposite
        2. Withdrawal
        3. Transter
        4. Balance Enquiries
        5. View Account details
        6. view your transaction history
        7. sign-out
        '''
        while True:
            account_balance = get_balance(id)
            print(f"\n Your current balance is {account_balance}")
            print(menu)
            response = input("Enter your response 1 to 7: ")
            if response == "1":
                deposit(id,name)

            elif response == "2":
                withdwawal(id,name)

            elif response == "3":
                tranfer_out(id)

            elif response == "4":
                balance_enquiry(id,name)

            elif response == "5":
                view_acc_details(id)

            elif response == "6":
                transactions(id)

            elif response == "7":
                loading("signing out")
                break
            else:
                print("please enter valid option as shown above")
                continue



def view_acc_details(id):
    name, acc_number, account_balance, = cursor.execute('SELECT full_name, account_number, account_balance FROM users WHERE id = ?', (id,)).fetchone()
    conn.commit
    loading("\n Getting account details")
    print(f"\n\n ACCOUNT NAME: {name} \n ACCOUNT NUMBER: {acc_number} \n ACCOUNT BALANCE: {account_balance}")



def balance_enquiry(id,name):
    balance = get_balance(id)
    loading('getting your balance pls wait')
    print(f"\n {name},your current balance is #{balance}")




def deposit(id,name):
        while True:
            try:
                 deposite_amount = int(input("How much do you want to deposite: #"))
            except ValueError:
                print("invalid input")
                continue
            except Exception as e:
                print("invalid input",e)
                continue

            if not deposite_amount:
                print("field cannot be left empty")
                continue

            if deposite_amount < 0:
                print("invalid amount you cant enter a negative value")
                continue

            break
    
        balance = get_balance(id)
        updated_balance = balance + deposite_amount
        update_balance(updated_balance,id)
        cursor.execute("INSERT INTO transactions (amount, type, user_id, balance) VALUES (?, ?, ?, ?)", (deposite_amount, "deposit", id, updated_balance,))
        conn.commit()
        loading("processing your deposite")
        print(f"{name}, #{deposite_amount} was succesfully added to your account")
      

def get_balance(id):
     get_balance = cursor.execute("SELECT account_balance, id FROM users WHERE id = ?",(id,)).fetchone()
     conn.commit()
     balance, id = get_balance
     return balance


def withdwawal(id,name):
    while True:
        current_balance = get_balance(id)
        if current_balance == 0:
            print(f'opps!!!!!  {name} your balance is #{current_balance}.00 insufficient funds')
            return_back('returning back to dashboard')
            break

        while True:

            try:
                enter_witdrawal_amount = input("Enter the amount you wish to withdraw: ")
                enter_witdrawal_amount = float(enter_witdrawal_amount)
            except ValueError as e:
                print("enter a valid amount")
                continue

            except Exception as e:
                print("An error occured",e)
                continue
            if enter_witdrawal_amount <= 100:
                print("transaction failed minimum withdrawal is #100")
                continue

            if enter_witdrawal_amount > current_balance:
                print(f"operation failed insufficient fund you can only witdraw upto  #{current_balance}")
                continue
            
    
            enter_witdrawal_amount = enter_witdrawal_amount + 50

            current_balance = current_balance - enter_witdrawal_amount
            update_balance(current_balance,id)
            try:
                cursor.execute("INSERT INTO transactions (amount, type, user_id, balance) VALUES (?, ?, ?, ?)", (enter_witdrawal_amount, "withdrawal", id,current_balance,))
                conn.commit()
            except sqlite3.IntegrityError as e:
                print("An error occured",e)
                continue
            except Exception:
                print("An error occured")
                continue


            
            loading("processing your transaction please wait")

            print(f"#{enter_witdrawal_amount} was withdrawn from your account")
            break

        break
        
def transactions(id):

    all_transactions = cursor.execute("SELECT * from transactions where user_id = ?",(id,)).fetchall()
    conn.commit()

    loading("Generating transaction history")

    num = 1

    for transaction in all_transactions:
       
        idd, date, amount, transaction_type, sender, balance, reciever, key, narration = transaction
        if sender is None and reciever is None:
            print(f"\n{num}. Date: {date}  Amount: #{amount}  Type: {transaction_type}  Balance: #{balance}")


        elif reciever is None:
            print(f"\n{num}. Date: {date}  Amount: #{amount}  Type: {transaction_type}  Sender name: {sender}     Description: {narration}  balance: #{balance}")


        elif sender is None:
            print(f"\n{num}. Date: {date}  Amount: #{amount}  Type: {transaction_type}  Receiver name: {reciever}  Description: {narration}  balance: #{balance}")

        num += 1

       
            
    

def update_balance(balance,id):
    cursor.execute("UPDATE users SET account_balance = ? where id = ?",(balance,id,))
    conn.commit()


def return_back(text):
        text = "returning back to menu"
        print(text, end='')
        for _ in range(12):
            sleep(0.3)
            print(".", end='', flush=True)
        print()


def loading(text):
    print(text, end='')
    for _ in range(12):
        sleep(0.3)
        print(".", end='', flush=True)
    print()
 

def tranfer_out(id):
    while True:
        account_of_receiver = input("enter the account number of the person you want to transfer to: ")
        pattern = r"^\d+$"
        match = re.match(pattern,account_of_receiver)

        if not match:
            print("enter a valid input")
            continue
        sender_account, = cursor.execute('SELECT account_number FROM users where id = ?',(id,)).fetchone()
        if sender_account == account_of_receiver:
            print("oppss you cant tranfer to yourself enter another account number")
            continue
        print('*****************',sender_account,account_of_receiver)

        conn.commit()
        account_checker = cursor.execute('SELECT full_name, id FROM users where account_number = ?',(account_of_receiver,)).fetchone()
        conn.commit()
        if account_checker is None:
            print("Account number is not correct")
            continue
        break


    while True:     
        receiver_name,receiver_id = account_checker
        print(f"receiver account name: {receiver_name}")
        while True:
            try:
                amount_sending = float(input("enter the amount you want to send: "))
                break
            except ValueError :
                print("opps please enter a valid amount")
                continue
            except Exception as e:
                print("opps error occured",e) 
                continue
        
        if amount_sending <= 0:
            print("enter a valid amount")
            continue

        description = input("enter narration: ")

        receiver_balance = get_balance(receiver_id)

        balance = get_balance(id)
        if balance == 0:
            print(f"oppss!!!!!! your balance is #{balance} you cant make any transfer")
            break
        if amount_sending > balance:
            print("insufficient funds to perform operation ")
            loading("returning to dashboard")
            break
        
        sender, = cursor.execute('SELECT full_name FROM users where id = ?',(id,)).fetchone()
        conn.commit()

        sender_name = sender
        
        balance = balance - amount_sending

        update_balance(balance,id)
        balance = get_balance(id)

        cursor.execute("INSERT INTO transactions (amount, type, user_id, balance, description, recipient) VALUES (?, ?, ?, ?, ?, ?)", (amount_sending, 'tranfer to', id,balance,description,receiver_name))
        conn.commit()
        
        receiver_balance = receiver_balance + amount_sending

        update_balance(receiver_balance,receiver_id)
        receiver_balance = get_balance(receiver_id)
        
        cursor.execute("INSERT INTO transactions (amount, type, user_id, balance, description, sender) VALUES (?, ?, ?, ?, ?, ?)", (amount_sending, 'transfer from', receiver_id,receiver_balance,description,sender_name))
        conn.commit()

        loading('processing transfer')
        print(f"transfer successfull, #{amount_sending} was sent to {receiver_name}")

        repeat_transfer = input("do you want to make another transfer? yes/no: ").strip().lower()
        if repeat_transfer == 'yes':
            continue
        elif repeat_transfer == 'no':
            return_back('returning to dashboard')
            break
        else:
            print('wrong input')
            return_back('returning to dashboard')
            break
 


while True:
    menu = """
    ******************************************UNITED BANK OF IBADAN (UBI)**********************************************

    which operation would u like to perform ?

    1.create an account with us today

    2.login if u already have an account

    3.exit

    4.Data policy 
    """
    print(menu)
    option = input("enter your choice 1 to 4: ")
    if option == "1":
        create_account()
    elif option == "2":
        login()
    elif option == "3":
        loading("Exiting site")
        break
    else:
        print("invalid input check options ")
        continue


