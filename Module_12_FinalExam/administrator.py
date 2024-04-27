
class Administrator:
    def __init__(self,bankName) -> None:
        self.bankName=bankName
        self.customerList={}
        self.admin={}
        self.loanList={}

    def add_customer(self,customer):
        self.customerList[customer.email]=customer
        print("Account Created Successfully!!! ")
    
    def add_admin(self,admin):
        self.admin['admin']=admin
    
    def system_login(self,email,password):
        for em in self.customerList.keys():
            if(em==email):
                if(password==self.customerList[em].password):
                    return self.customerList[em]
        return False

    def admin_login(self,email,password):
        return self.admin['admin'].email==email and self.admin['admin'].password==password