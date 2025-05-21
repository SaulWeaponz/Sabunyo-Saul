#create an atm withdrawal program to use if else statement to check account balance before withdrawals

password = "sswpnz"
balance = 900000
while True:
    passwordinput = input("Enter your password:")
    
    if passwordinput == password:
        print("Welcome to Saul Withdraw System")
        print("withdraw")
        print("cancel")
        choice = input("Enter your choice:")
        if choice == "withdraw":
            amountToWithdraw = int(input("Enter Amount to withdraw:"))
            if amountToWithdraw >= balance:
                print("Insufficient Balance.")
            else:
                balance = balance-amountToWithdraw
                print("You have remained with : "+str(balance))
        break
    else:
        print("Retry again with a correct password.")

