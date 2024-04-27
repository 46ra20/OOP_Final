from abc import ABC
class User(ABC):
    def __init__(self,name,email,password,address) -> None:
        self.name=name
        self.email=email
        self.password=password
        self.address=address
        super().__init__()
