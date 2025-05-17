class online_payment_system:
    def __init__(self,balance = 2000):
        self.balance = balance
        self.correct_pin = "1221"

    def deposit(self,amount):  # To Deposit money in Account
        while True:
            pin2 = input("Enter Pin :")
            if pin2 == self.correct_pin:
                if amount >= 0:
                    self.balance += (amount)
                    print(f"Deposited : ₹{amount} Succesfully")
                    print(f"Net Balance : ₹{self.balance}")
                    break
                else:
                    print("Enter Positive Number")
            else:
                print("Incorrect Pin  ❌")

    def check_Balance(self): #To check Balance
        while True:
            pin3 = input("Enter Pin :")
            if pin3 == self.correct_pin:
                print(f"Your Bank Balance is : ₹{self.balance}")
                break
            else:
                print("Incorrect Pin  ❌")

    def send_money(self):  # To send Money
        while True:
            while True:
                mob_no = (input("Enter Mobile Number :"))
                if len(mob_no) != 10 or not mob_no.isdigit():
                    print("Invalid Mobile Number !!")
                else:
                    break
            money_to_send = float(input("Enter amount To send :"))
             # allow 3 attempts for pin
            for attempt in range(3):
                pin4 = input("Enter PIN: ")
                if pin4 == self.correct_pin:
                    self.balance -= money_to_send
                    print("✅ Payment Done Successfully")
                    print(f"Remaining Balance: ₹{self.balance}")
                    return
                else:
                    print(f"Incorrect PIN ❌ ({2 - attempt} attempts left)")
        
            print("❌ Transaction Failed: Too many incorrect PIN attempts.")
            return
        
    def run_system(self):  # To Run This overall Sytem
        while True:
            print("\n---ONLINE PAYMENT SYSTEM---")
            print("\n1.Send Money")
            print("2.Check Balance")
            print("3.Deposite Money")
            print("4.Exit")

            choice = input("Enter Your Choice (1-4) :")

            if choice == "1":
                self.send_money()
            elif choice =="2":
                self.check_Balance()
            elif choice == "3":
                amount = float(input("Enter Amount To Deposit :"))
                self.deposit(amount)
            elif choice =="4":
                print("Thanks For Using This System")
                break
            else:
                print("Invalid Input ❌ ")

    def open_system(self):  #To open This system
        while True:
            pass1 = input("Enter Pin To Open To system :")
            if pass1 == self.correct_pin :
                self.run_system()
                break
            else:
                print("Incorrect Pin ❌")

obj = online_payment_system(balance = 2000)
obj.open_system()
