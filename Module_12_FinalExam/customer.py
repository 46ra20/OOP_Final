from user import User
from datetime import datetime

class Customer(User):
    def __init__(self, name, email,password, address,accountType,administrator) -> None:
        self.accountType=accountType
        self.balance=0
        self.id=len(administrator.customerList)+1000
        self.takeLoan=0
        self.transactionHistory=[]
        super().__init__(name, email,password, address)

    # customer deposit his account
    def deposit(self,email,amount,administrator):
        if(amount>0):
            administrator.customerList[email].balance+=amount
            self.transactionHistory.append([self.id,datetime.now().date(),datetime.now().strftime('%H:%M:%S'),amount,"Deposit"])
            print(f"Your Current Balance: {self.balance}")
        else:
            print("Sorry, You can not deposit negative value.")
    
    # customer withdrawal form his account
    def withdrawal(self,email,amount,administrator):
        if(amount>administrator.customerList[email].balance):
            print("Withdrawal amount exceeded")

        else:
            if(administrator.admin['admin'].isBankRupt):
                print("Bank is bankrupt")
            else:
                administrator.customerList[email].balance-=amount
                self.transactionHistory.append([self.id,datetime.now().date(),datetime.now().strftime('%H:%M:%S'),amount,"Withdraw"])
                print(f"Money Withdraw is Complete. Your Current Balance {administrator.customerList[email].balance}")
    
    # check balance
    def check_balance(self,email,administrator):
        if(administrator.admin['admin'].isBankRupt):
                print("Bank is bankrupt")
        else:
            print(f'Your Current Balance is: {administrator.customerList[email].balance} Taka Only')

    # check transaction history
    def check_transaction_history(self):
        if(not self.transactionHistory):
            print("No transaction history!!!")
        else:
            print(f"ID\tDate\tTime\tAmount\tTransaction Type")
            for tran in self.transactionHistory:
                print(*tran,sep='\t')

    #take loan
    def take_loan(self,email,amount,administrator):
        ad = administrator.admin

        if(ad['admin'].isLoanActive):
            if(self.takeLoan<2):
                administrator.loanList[email]=[email,self.id,datetime.now().date(),datetime.now().strftime('%H:%M:%S'),amount]
                self.transactionHistory.append([self.id,datetime.now().date(),datetime.now().strftime('%H:%M:%S'),amount,"Bank Loan"])
                
                self.balance+=amount
                self.takeLoan+=1
                print(f"You Take Loan From Bank. Current Balance {self.balance} Taka Only")
            else:
                print("You Can not take lone more than two times.")
        else:
            print("Sorry, Loan service not active at this moment")
    
    # send money 
    def  send_money(self,r_email,amount,administrator):
        if(administrator.admin['admin'].isBankRupt):
                print("Bank is bankrupt")
        else:
            # ad = administrator.customerList
            for em in administrator.customerList.keys():
                if(em == r_email):
                    if(administrator.customerList[self.email].balance>=amount and amount>0):
                        administrator.customerList[r_email].balance+=amount
                        administrator.customerList[self.email].balance-=amount

                        self.transactionHistory.append([self.id,datetime.now().date(),datetime.now().strftime('%H:%M:%S'),amount,f"Send Money {administrator.customerList[r_email].name}"])
                        print(f"Send money successfully done !!!. Current Balance {self.balance}")
                        administrator.customerList[r_email].transactionHistory.append([administrator.customerList[r_email].id,datetime.now().date(),datetime.now().strftime('%H:%M:%S'),amount,f"Receive Money from {self.name}"])
                        # print(f"Send money successfully done !!!. Current Balance {self.balance}")
                    else:
                        print("Invalid amount")
                    return
            
            print("Sorry, No user exist with this email")
    

