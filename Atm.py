class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.pin = "1234"

    def verify_pin(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Invalid PIN!")
            return False

    def display_menu(self):
        print("\n ATM MENU ")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def check_balance(self):
        print(f"Your current balance is: {self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"{amount:.2f} deposited successfully.")
            else:
                print("Enter a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Enter a valid amount.")
            elif amount > self.balance:
                print("Insufficient balance!")
            else:
                self.balance -= amount
                print(f"{amount:.2f} withdrawn successfully.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def run(self):
        if not self.verify_pin():
            return

        while True:
            self.display_menu()
            choice = input("Select an option (1-4): ")
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select again.")

# Run the ATM
atm = ATM(initial_balance=1000.00)
atm.run()
