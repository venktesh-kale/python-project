# ATM simulation program

balance = 100000
pin = '0000'
max_attempts = 5
attempts = 0


def display_menu():
    print("Welcome to the ATM")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Transfer Money")
    print("4. Change PIN")
    print("5. Reset ATM")
    print("6. Quit")


def check_pin():
    global attempts
    while True:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == pin:
            return True
        else:
            attempts += 1
            if attempts >= max_attempts:
                print("You have exceeded the maximum number of attempts. ATM locked.")
                return False
            print("Incorrect PIN. Please try again.")


def check_balance():
    print(f"Your balance.txt is N{balance}")


def withdraw_money():
    global balance
    amount = int(input("Enter the amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print(f"Withdrawn N{amount}. Your new balance.txt is N{balance}")
    else:
        print("Insufficient balance.txt.")


def transfer_money():
    global balance
    amount = int(input("Enter the amount to transfer: "))
    if amount <= balance:
        recipient_account = input("Enter the recipient's account number: ")
        print(f"Transferred N{amount} to account {recipient_account}.")
        balance -= amount
        print(f"Your new balance.txt is ${balance}")
    else:
        print("Insufficient balance.txt.")


def change_pin():
    global pin
    new_pin = input("Enter your new 4-digit PIN: ")
    if len(new_pin) == 4 and new_pin.isdigit():
        pin = new_pin
        print("PIN successfully changed.")
    else:
        print("Invalid PIN format. Please enter a 4-digit number.")


def reset_atm():
    global balance, pin, attempts
    balance = 100000
    pin = '0000'
    attempts = 0
    print("ATM has been reset. Balance set to $100,000 and PIN reset to '0000'.")


while True:
    display_menu()
    option = input("Enter your choice: ")

    if option == '1':
        if check_pin():
            check_balance()
    elif option == '2':
        if check_pin():
            withdraw_money()
    elif option == '3':
        if check_pin():
            transfer_money()
    elif option == '4':
        if check_pin():
            change_pin()
    elif option == '5':
        reset_atm()
    elif option == '6':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
