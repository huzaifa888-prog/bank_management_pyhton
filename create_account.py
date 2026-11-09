all_accounts = []

def create_account(full_name:str, father_name:str, cnic:str, phone:str,balance:int, pin:int):
    account={
        "Full name": full_name.capitalize(),
        "Father's name": father_name.capitalize(),
        "Cnic": cnic,
        "Phone": phone,
        "Balance": balance,
        "Pin":pin
            }
    all_accounts.append(account)
    return all_accounts


def all_the_accounts():
    for account_number,accounts in enumerate(all_the_accounts):
        print(f'''~~~~~~~~~~~~~~~~~~~~ALL THE ACCOUNTS ARE GIVEN BELOW~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n''')
        print(f'''
            Account Number: {account_number["Account_number"]}
            Full Name: {accounts["Full name"]}
            Father's Name: {accounts["Father's name"]}
            CNIC: {accounts["Cnic"]}
            Phone: {accounts["Phone"]}
            Balance: {accounts["Balance"]} PKR
                ''')


def check_balance(name:str, pin:int):

    for accounts in all_accounts:
        if name.lower() == accounts["Full name"].lower() and pin == accounts["Pin"]:
            return f"Login Successful! \n Your Balance: {accounts['Balance']} PKR" 
    
    return"Invalid user or pin "


def deposit_money(name:str, pin:int, cash:int):
    for accounts in all_accounts:
        if name.lower() == accounts["Full name"].lower() and pin == accounts["Pin"]:
            if cash > 200:
                accounts["Balance"]+=cash
                return f"Your cash is Deposit Successfully..!\n{accounts['Balance']} PKR"
            
            
            return "Cash must be grater than 200"

    return "Invalid user or pin "


def withdraw_money(name:str,pin:int,amount:int):

    for accounts in all_accounts:

        if name.lower() == accounts["Full name"].lower() and pin == accounts["Pin"]:

            if amount > 0 and amount <= accounts["Balance"]:

                accounts["Balance"] -= amount

                return f"""
                Withdrawal Successful!

                Withdrawn Amount: {amount} PKR
                Remaining Balance: {accounts["Balance"]} PKR
                """
            
            
            return f"Your initial balance is {accounts['Balance']}, insufficient balance!"
            
        
    return "Invalid user or pin "


def transfer_money(sender_name:str, sender_pin:int, reciver_account:str, sender_balance:int, amount:int):

    sender = None
    reciver = None

    # Find Sender: 
    
    for accounts in all_accounts:
          if (sender_name.lower() == accounts["Full name"]) and sender_pin == accounts["Pin"]:
                sender = accounts
                break

    # Find Reciver:
    for accounts in all_accounts:
          if accounts["Account_number"] == reciver_account:
                reciver = accounts

    # Check Sender:

    if sender is None:
          return "Invalid Sender name or pin"

    # Check Reciver:

    if reciver is None:
          return "Reciver Account Not Found..!"

    # Check Same Account:            

    if sender == reciver:
          return "You cannot transfer Money to your own account..!"
    
    # Check Amount And Balance:

    if amount < 200:
          return "Minimum transfer amount is 200 PKR!"

    if amount >= sender["Balance"]:
          return "Insufficient Balance..!"

    # Transfer Money: 
    sender_balance["Balance"] -= amount
    reciver["Balance"] += amount
    return f'''
    Transfer Successful!

    Sender: {sender["Full name"]}
    Receiver: {receiver["Full name"]}
    Transferred Amount: {amount} PKR

    Sender Remaining Balance: {sender["Balance"]} PKR
    Receiver New Balance: {receiver["Balance"]} PKR
    '''
    

def transaction_history():
    pass


def account_details():
    pass


def chnage_pin():
    pass


def exit():
    return "Thank you for using SMIT Bank. Have a great day!"

is_running = True
while is_running:
    print('''
    =============================================================================
    --------------------------WELCOME TO SMIT BANK------------------------------\n
    ``````````````````````````CHOOSE THE BUTTONS````````````````````````````````\n
            =======================================================
                         PLEASE SELECT AN OPTION
            =======================================================\n\n
  Press : [1]  Create Account
  Press : [2]  All Accounts 
  Press : [3]  Check Balance
  Press : [4]  Deposit Money
  Press : [5]  Withdraw Money
  Press : [6]  Transfer Money
  Press : [7]  Transaction History
  Press : [8]  Account Details
  Press : [9]  Change PIN
  Press : [10]  Exit

''')

    choice = int(input("Enter your choice (1-10): "))


    if choice == 1:
        full_name = input("Apna Full Name enter karein: ")
        father_name = input("Apne Father's Name enter karein: ")
        cnic = input("Apna CNIC enter karein: ")
        phone = input("Apna Phone Number enter karein: ")
        balance = int(input("Apna balance batain: "))
        pin = int(input("Apni pin batain: "))
        print(create_account(full_name,father_name,cnic,phone,balance,pin))

    elif choice == 2:
        print(all_accounts())

        
    elif choice == 3:
        name = input('Apna pura name likein: ')
        pin = int(input('Apna Pin likein: '))
        print(check_balance(name,pin))


    elif choice == 4:
        name = input("Apna pura nam likein: ").lower()
        pin = int(input("Apni pin likein: "))
        cash = int(input("Apna cash dalein: "))
        print(deposit_money(name,pin,cash))


    elif choice == 5:
        name = input("Apna pura nam likein: ").lower()
        pin = int(input("Apni pin likein: "))
        withdraw_amount = int(input("Apna cash dalein: "))
        print(withdraw_money(name,pin,withdraw_amount))


    elif choice == 6:
        sender_name = input("Sender ka naam likhein: ")
        sender_pin = int(input("Sender ki PIN likhein: "))
        receiver_account = input("Receiver ka account number: ")
        amount = int(input("Transfer amount likhein: "))
        print(transfer_money(
        sender_name,
        sender_pin,
        receiver_account,
        amount
    ))


    elif choice == 9:
        is_running = False
        print(exit())

else:
    print("Invalid choice. Please try again.")