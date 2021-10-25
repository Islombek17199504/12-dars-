# def tuliq_ism_yasa(ism,familiya):
#     """tuliq ism yasash funksiyasi"""
#     tuliq_ism = f"{ism} {familiya}"
#     return tuliq_ism

# talab = tuliq_ism_yasa('Olimov', 'Hakimov')
# print(talab)

# def tuliq_ism_yasa(ism,familiya,otasining_ismi=''):
#     """tuliq ism yasash otasining ismini ham qushib quyish"""
#     if otasining_ismi:
#         tuliq_ism = f"{ism} {familiya} {otasining_ismi}"
#     else:
#         tuliq_ism = f"{ism} {familiya}"
#     return tuliq_ism.title()
# talaba = tuliq_ism_yasa('Anvar', 'Qoraboyev')
# print(f"{talaba} bugun darsga kech kelib turdi")
    
# def oraliq(min,max,qadam):
#     sonlar =[]
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(10, 20))

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
# !   avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto


# def shaxs_malumot(ism, familiya, t_yil, y_joy, email, tel):
#     shaxs = {'ism':ism,
#              'familiya':familiya,
#              'tugulgan yil':t_yil,
#              'yashash joy':y_joy,
#              'email':email,
#              'tel':tel}
#     return shaxs


# foydalanuvchi = []

# while True:
#     print("\nquyidagi malumotlarni kiritinf\n")
#     ism = input('Ismingiz nima>>> ')
#     familiya = input('familiyangiz nima>>> ')
#     t_yil = input('Tugilgan yilingiz qaysi>>> ')
#     y_joyi = input('Yashash manzilingiz:>>> ')
#     email = input('Elektron pochta manzilingiz>>> ')
#     teli = input('Telefon raqamingiz>> ')
        
#     foydalanuvchi.append(shaxs_malumot(ism, familiya, t_yil, y_joyi, email, teli))
        
#     javob = input('Yana foydalanuvchi qushasizmi?(yes\no): ')
#     if javob == 'no':
#         break
    
# print(f"{ism} {familiya} {t_yil} yil da tugilgan hozirda {y_joyi} shahrida yashaydi electron manzili {email} tel {teli} ")

# def son_katta(son1,son2,son3):
#     if son1 < son2:
#         son = son2
#     elif son2 < son3:
#         son = son3
#     else:
#         son = son1
#     return son
# print(son_katta(2, 2, -4))


# def aylana_radius(radius,diametr,yuzi):
#     aylan = {'radiusi':radius,
#              'diametri':diametr,
#              'yuzi':yuzi}
#     return aylan
    
# radiusi = int(input('Aykana radiusini kiriting::>>>'))
    
# print(f"Aylananing radiusi {radiusi} diametri {radiusi*2} ga yuzi ese {(radiusi**2)*3.14}")



# def tup_son_top(min,max):
#     tup_son = []
#     for n in range(min,max+1):
#         tup =True
#         if (n==1):
#             tup = False
#         elif (n==2):
#             tup = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tup = False
#         if tup:
#             tup_son.append(n)
#     return tup_son

# # print(tup_son_top(1, 20))

# def fibonachi(n):
#     sonlar =[]
#     for x in range(n):
#         # if x==0 or x==1:
#         #     sonlar.append(1)
#         # else:
#         #     sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# son = int(input('Ixtiyoriy son kiriitng:::>>> '))
# print(fibonachi(son))





























