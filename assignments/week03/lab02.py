# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        choice = input("Choose option: ")
        # Complete the menu logic here
        # Your code here:
        
        if choice == "1":
            print("Your balance = ", balance)
            
        if choice == "2":
            amount = float(input("Withdraw amount:"))
            if amount < 0:
                print("cannot deposit less than 0")
            else:
                balance = balance - amount
                print("Your balance now =", balance)
            print("Plase collect your money,and your balance now = ",balance)
            
        if choice == "3":
            amount = float(input("Deposit amount:"))
            if amount < 0:
                print("cannot deposit less than 0")
            else:
                balance = balance + amount
                print("Your balance now =", balance)
                
        if choice == "4":
            break
        else:
            continue
else:
    print("Invalid PIN")