
# print('yaqin dustlar ruyxati')
# ismlar = []
# n = 1
# while True:
#     savol = f'{n} - Dustingizni ismini kiritin:'
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input('Yana dustingizni kiritasizmi: (ha\yoq)')
#     n+=1
#     if takrorlash != 'ha':
#         break
    
# print('Dostlaringiz ruyxati')
# for ism in ismlar:
#     print(ism.title())


# print('Dustingizni yoshini saqlaymiz')

# dustlar = {}

# ishora = True

# while ishora:
#     ism = input('Dustingizni ismi:: ')
#     yosh = input(f'{ism.title()}ning yoshini kiriting::>>> ')
#     dustlar[ism] = int(yosh)
    
#     javob = input('Yana dostingiz kiritasizmi,(ha\yoq)::>>>')
#     if javob == 'yoq':
#         ishora = False
# for ism,yosh in dustlar.items():
# #     print(f'{ism.title()} {yosh} yoshida')
        
    
# cars = ['nexia','matiz','nexia','lacetti','malibu','nexia']
# print(cars)
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)


# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
    
   
    

# mahsulotlar =[]

# while True:
#     buyurtma = input('Mahsulot buyurtma bering:::>>> ')   
#     mahsulotlar.append(buyurtma)
    
#     javob = input('Yana mahsulot qushasizmi,(ha\yoq)::>>>')
#     if javob != 'ha':
#         break
# #         break
# print(mahsulotlar)

# mahsulotlar = {}
# while True:
#     mahsulot = input("Mahsulot nomini kiriting: ")
#     narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
#     mahsulotlar[mahsulot] = narh
#     javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
#     if javob != 'ha':
#         break

mahsulotlar = {}

while True:
    mahsulot = input("Mahsulotni nomini kiriting:::>>> ")
    narh = input(f"{mahsulot.title()}ning narhini kiriitng:::>>>")
    mahsulotlar[mahsulot] = narh
    javob = input('Yana mahsulot kiritasizmi,(ha\yoq):::>>> ')
    if javob != 'ha':
        break




























