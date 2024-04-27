from customer import Customer
from administrator import Administrator
from admin import Admin

my_bank = Administrator('My Bank')
admin = Admin(name='Admin',email='admin@gmail.com',password='1234',address='Dhaka')

my_bank.add_admin(admin)

# print(my_bank.admin)
# replica system for this project


# user section
def customerLoginSystem(user,email):

    if(user):
        print("\n--------------------------------------------------")
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Available Balance")
            print("4. Transaction History")
            print("5. Take Loan From Bank")
            print("6. Send Money")
            print("7. Log Out")

            cho = int(input("Enter Your Choice: "))

            if(cho==1):
                amount = int(input("Enter Your Amount: "))
                user.deposit(email,amount,my_bank)
            elif cho==2:
                amount = int(input("Enter Your Amount: "))
                user.withdrawal(email,amount,my_bank)
            elif cho==3:
                user.check_balance(email,my_bank)
            elif cho==4:
                user.check_transaction_history()
            elif cho==5:
                amount=int(input("Enter Your Amount: "))
                user.take_loan(email,amount,my_bank)
            elif cho==6:
                em  = input("Enter Email, You Want to Send Money: ")
                amount  =int(input("Enter Your Amount: "))
                user.send_money(em,amount,my_bank)
            elif(cho==7):
                break
            else:
                print("Invalid Choice!!!")
        print("--------------------------------------------------\n")
        
    else:
        print("No user available with this Email and Password!!!")

def login_or_registration():
    while True:
        print("1. Login")
        print("2. Registration")
        print("3. Exit")
        x = int(input("Enter your choice: "))
        if(x==1):
            email = input("Enter Your Email: ")
            password = input("Enter Your Password: ")
            user = my_bank.system_login(email=email,password=password)
            customerLoginSystem(user=user,email=email)

        elif(x==2):
            # name, email,password, address,accountType,administrator
            name = input("Enter Your Name: ")
            email=input("Enter Your Email: ")
            password = input("Enter Your Password: ")
            address= input("Enter Your Address: ")
            accountType = input("Enter Your Account Type(Current or Saving): ")

            user = Customer(name=name,email=email,password=password,address=address,accountType=accountType,administrator=my_bank)
            my_bank.add_customer(user)
            customerLoginSystem(user=user,email=email)
        elif x==3:
            print("Thank's for Using Our Service")
            break

# admin section
def adminLogin():
    email = input("Enter Your Email: ")
    password = input("Enter Your Password: ")

    ad = my_bank.admin_login(email=email,password=password)
    if(ad):
        while True:
            print("\n1. Create Customer Account")
            print("2. Delete Customer Account")
            print("3. All User")
            print("4. Available Balance in Bank")
            print("5. Total Loan")
            print("6. Loan Future")
            print("7. Is Bankrupt")
            print("8. Logout\n")

            x = int(input('Enter Your Choice: '))

            if(x==1):
                name = input("Enter Customer Name: ")
                email=input("Enter Customer Email: ")
                password = input("Enter Customer Password: ")
                address= input("Enter Customer Address: ")
                accountType = input("Enter Customer Account Type(Current or Saving): ")

                user = Customer(name=name,email=email,password=password,address=address,accountType=accountType,administrator=my_bank)
                my_bank.add_customer(user)
            elif x==2:
                email = input("Enter Customer Email for Delete: ")
                admin.delete_account(email=email,administrator=my_bank)
            elif x==3:
                admin.all_users_list(my_bank)
            elif x==4:
                admin.total_available_balance(my_bank)
            elif x==5:
                admin.total_loan_amount(my_bank)
            elif x==6:
                if(not admin.isLoanActive):
                    print("Loan Service is Deactivate, Do you want to active this?")
                    y = input("Enter (y/n): ")
                    if(y.lower()==y):
                        admin.on_off_loan_service(my_bank)
                else:
                    print("Loan Service is Active, Do you want to deactivate this?")
                    y = input("Enter (y/n): ")
                    if(y.lower()==y):
                        admin.on_off_loan_service(my_bank)

            elif x==7:
                if(admin.isBankRupt):
                    print("Bank Is Bankrupt, Do you Want To active Agin ?")
                    y = input("Enter (y/n): ")
                    if(y.lower()==y):
                        admin.is_bankRupt()
                else:
                    print("Bank Is Not Bankrupt, Do you Want To Declare as Bankrupt?")
                    y = input("Enter (y/n): ")
                    if(y.lower()==y):
                        admin.is_bankRupt()
            elif x==8:
                break
            else:
                print("Invalid Option")

            
    else:
        print("Invalid ID and Password")


while True:
    print("--------Welcome to our system, Choice An Option--------")
    print("1. Login or Registration")
    print("2. Exit")
    x = int(input("Enter Your Choice: "))
    if(x==1):
        print("1. Admin")
        print("2. Customer")
        choice = int(input("Enter Your Choice: "))

        if(choice==1):
            print("\n-------------------Admin Section-------------------")
            adminLogin()
            print("------------------------Exit------------------------\n")
            
        elif(choice==2):
            print("\n-------------------User Section-------------------")
            login_or_registration()
            print("-----------------------Exit-----------------------\n")
        else:
            print("Invalid Choice!!!")
    else:
        break
