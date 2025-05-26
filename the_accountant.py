class Account:
    def __init__(self):
        try:
          name = input("enter your name: ")
          balance = int(input("enter your balance"))
          self.name = name
          self.balance = balance
        except Exception as e:
            print(e)



    def deposite(self):
        added_amount = int(input("enter the amount you want to deposite: "))
        self.balance += added_amount
        print(f"your current balance is ${self.balance}")
    
    
    def withdraw(self):
        while True:
            withdrawal_amount = int(input("enter the amount you want to withdraw"))
            if withdrawal_amount > self.balance:
                print(f"opps insufficient balance re-enter amount current balance is {self.balance}")
                continue
            else:
                self.balance -= withdrawal_amount
                print(f"{withdrawal_amount} removed succesfullly, current balance is {self.balance}")
                break


# account1 = Account()
# account1.deposite()
# account1.withdraw()
while True:
  try:
      numb1 = int(input("enter number:"))
      numb2 = int(input("enter number"))
      result = numb1 / numb2
      print(result)
      break
  except Exception as e:
    print("an error occured",e)
    # continue

# print(result)

