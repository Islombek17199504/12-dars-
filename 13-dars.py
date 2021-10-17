# yosh = float(input('Yoshingiz nechida:>>>'))
# if yosh < 4 or yosh > 60:
#     print('Sizga kirish bepul')
# elif yosh < 18:
#     print('Sizdan 10000 sum')
# else:
#     print('Sizdan 20000 sum')

# son_a = float(input('Birirnchi sonni kiriting:>>>'))
# son_b = float(input('Ikkinchi sonni kiriting:>>>'))
# if son_a == son_b:
#     print('Sonlar teng')
# elif son_a > son_b:
#     print('Birinchi son katta')
# else:
#     print('Ikkinchi son katta')


# mahsulotlar = ['piyoz', 'sabzi', 'olma', 'guruch', 'pomidor', 'bodom' ,'behi','kartoshka']
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1} - mahsulotni qoshing>>>'))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f'Dokonimizda {mahsulot} bor')
#     else:
#         print(f'Dokonmizda {mahsulot} yoq')

# mahsulotlar = ['olma','behi','nok','anor','uzum','banan','shaftoli','xurmo','sabzi']
# savat = []
# for n in range(5):
#     savat.append(input('Mahsulotni kiriting:>>>'))
    
# bor_mahsulotlar = []
# mavjud_emas = []    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print(f'Dokonimizda quyidagi mahsulotlar yoq')
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print('Siz suragan mahsulot dokonimizda yoq')

# usur = ['anvar', 'bobo', 'islom', 'sarvar']
# login = input('Yangi loginni kiriting:>>>')

# if login.lower() in usur:
#     print('Login band, yangi login kiriting')
# else:
#     print(f'Hush kelibsiz {login.title()}!')



# users = ['alisher','aziza','yasina','umar']

# login = input("Yangi login tanlang: ")

# if login.lower() in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")


son = int(input('Islatgan sonni kiriting:>>>'))
 
for n in range(2,11):
    if not (son%n):
        print(f'{son} soni {n} ga qoldiqsiz bulinadi!')










