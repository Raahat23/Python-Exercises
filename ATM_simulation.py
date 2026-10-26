# ATM simulation

# Defining constants: users_pin and account starting balance
PIN = "1234"
BALANCE = 10000.00

# defining the main function
def main():
    # Ask user for their PIN
    pin = input("Enter your PIN: ")

    # check if user entered PIN is correct
    if pin == PIN:
        menu(BALANCE)
    else:
        print("Incorrect PIN")
        return

# defining the ATM menu function
def menu(BALANCE):
    # Ask user for the task they want to perform
    choice = input("Select an option(1-4) to perform a task:\n1.CHECK BALANCE\n2.WITHDRAWAL\n3.DEPOSIT\n4.EXIT\n")

    # checking which option was selected
    while choice != "4":
        if choice == "1":
            print(f"Account Balance: {BALANCE}")
        elif choice == "2":
            w_amount = float(input("Enter an amount to withdraw: "))
            if w_amount > 0 and w_amount <= BALANCE:
                BALANCE = BALANCE - w_amount
                print(f"Withdrawal of {w_amount} successful.\nRemember to take your card before leaving")
            else:
                print("Invalid amount entered. Try again!!!")
        elif choice == "3":
            deposit_amount = float(input("Enter the amount to deposit: "))
            if deposit_amount > 0:
                BALANCE = BALANCE + deposit_amount
                print(f"Current Balance: {BALANCE}")
            else:
                print("Invalid amount entered. Amount should be greater than 0.")
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option entered. Try Again!!!")
        # Ask use if the want to perform another transaction
        transaction = input("Would you like to perform another transaction?(Y/N): ").upper()
        if transaction == "Y":
            choice = input("Select an option(1-4) to perform a task:\n1.CHECK BALANCE\n2.WITHDRAWAL\n3.DEPOSIT\n4.EXIT\n")
        else:
            break

#calling the main function
main()