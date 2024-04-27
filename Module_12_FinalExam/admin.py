from user import User
from customer import Customer

class Admin(User):
    def __init__(self, name, email,password, address) -> None:
        self.isBankRupt = False
        self.isLoanActive=True
        super().__init__(name, email,password, address)

    # admin can create user account
    def create_user_account(self,name, email,password, address,accountType,administrator):
        name  = Customer(name,email,password,address,accountType,administrator)
        administrator.add_customer(name)
    # admin can delete any account
    def delete_account(self,email,administrator):
        for em in administrator.customerList.keys():
            if(em==email):
                del(administrator.customerList[email])
                print("User Delete Successfully!!!")
                return
        else:
            print("No user found")

    # all users list
    def all_users_list(self,administrator):
        if(not administrator.customerList):
            print("No customer yes!!!")
        else:
            print("ID\tName\tEmail\tBalance\tAddress\tAccount Type")
            for v in administrator.customerList.values():
                print(f"{v.id}\t{v.name}\t{v.email}\t{v.balance}\t{v.address}\t{v.accountType}")
    # total available balance
    def total_available_balance(self,administrator):
        if(not administrator.customerList):
            print("No bank balance yet!!!")
        else:
            total_balance = 0
            for v in administrator.customerList.values():
                total_balance += v.balance
            print("Total Balance :",total_balance,"Taka only")
    
    #total loan amount
    def total_loan_amount(self,administrator):
        if(not administrator.loanList):
            print("No loan yet!!!")
        else:
            total_loan = 0
            for v in administrator.customerList.values():
                total_loan += v.balance
            print("Total Loan :",total_loan,"Taka only")
        
    # on off loan service
    def on_off_loan_service(self,administrator):
        # print(administrator.admin['admin'].isLoanActive)
        administrator.admin['admin'].isLoanActive = not administrator.admin['admin'].isLoanActive
        return administrator.admin['admin'].isLoanActive
    # bankrupt
    def is_bankRupt(self):
        self.isBankRupt= not self.isBankRupt

    #loan list
    def loan_list(self,administrator):
        pass
            
