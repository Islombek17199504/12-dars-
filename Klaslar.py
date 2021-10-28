# class Talaba:
#     def __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
    
#     def get_age(self,yil):
#         return yil - self.tyil
       
#     def get_name(self):
#         return self.ism
        
#     def tanishtir(self):
#         return f"Ismim {self.ism} {self.familiya} tugilgan yilim {self.tyil}"
        
# talaba1 = Talaba('Olim', 'Olimov', 2020)

class User:
    def __init__(self,ism,userism,email):
        self.ism = ism
        self.uism = userism
        self.mail = email
        
        
    def get_fullname(self):
        return f"{self.ism}"
        
    def get_info(self):
        return f"Foydalanuvchi:{self.ism}, ismi: {self.uism}, email:{self.mail}"
        
        
user1 = User('Anvar1995', 'Anvar Qoraboyev', 'anvarqoraboyev@gmail.com')       