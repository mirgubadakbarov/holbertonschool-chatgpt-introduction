class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds to complete the withdrawal. You tried to withdraw ${amount:.2f}, but your current balance is ${self.balance:.2f}.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

def handle_deposit(cb):
    try:
        amount = float(input("Enter the amount to deposit: $"))
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            cb.deposit(amount)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def handle_withdraw(cb):
    try:
        amount = float(input("Enter the amount to withdraw: $"))
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            cb.withdraw(amount)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm == 'yes':
                print("Goodbye!")
                break
        elif action == 'deposit':
            handle_deposit(cb)
        elif action == 'withdraw':
            handle_withdraw(cb)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
