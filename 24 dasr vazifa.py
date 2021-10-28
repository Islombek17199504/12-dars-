# class Shaxs:
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
        
        
#     def get_info(self):
#         info = f"{self.ism} {self.familiya} Passport: {self.passport} tug'ilgan yili {self.tyil}"
#         return info
    
    
        
# talaba1 = Shaxs('Alijon', 'Alijonov', 'AB1234567', 2021)
        

# class Professor(Shaxs):
#     def __init__(self, ism, familiya, passport, tyil,idraqam,manzil):
#         super().__init__(ism,familiya,passport,tyil)
#         self.idraqam = idraqam
#         self.manzil = manzil
        
#     def get_id(self):
#         return self.idraqam
    
#     def get_info(self):
#         info = f"{self.ism} {self.familiya} Passport: {self.passport} tug'ilgan yili {self.tyil}"
#         info += f" ID raqami {self.idraqam} Turar joyi: {self.manzil}"
#         return info
        
# class Manzil:
#     def __init__(self,uy,kucha,tuman,viloyat):
#         self.uy = uy
#         self.kuch = kucha
#         self.tuman = tuman
#         self.viloyat = viloyat
        
#     def get_manzil(self):
#         manzil = f"{self.viloyat} viloyati {self.tuman} tumani {self.kuch} kuchasi {self.uy} xonadon" 
#         return manzil
# manzil_uy = Manzil(24, "Marifat", 'Fargona', 'Fargona')   
# talaba1 = Professor('Alijon', 'Alijonov', 'AB1234567', 2021, 123456, manzil_uy)



# class Foydalanuvchi(Shaxs):
#     def __init__(self, ism, familiya, passport, tyil):
#         super().__init__(ism, familiya, passport, tyil)
        
        
    
# # foydalanuvchi1 = Foydalanuvchi('Bobomurod', 'Nazir', 'AA1234567', 1995)



# class Admin(Foydalanuvchi):
#     def __init__(self, ism, familiya, passport, tyil):
#         super().__init__(ism, familiya, passport, tyil)
        
        
#     def ban_user(self):
#         return f"Foydalanuvchi bloklandi"
        

        
# foydalanuvchi1 = Admin('Anvar', 'Nazir', 'AA1234567', 1995)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        