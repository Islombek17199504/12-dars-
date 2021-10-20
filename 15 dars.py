# Alisher_Navoiy = {
#                 'ism':'Alisher navoiy',
#                 't_yil':1441,
#                 'y_joy':'samarqand',
#                 'asarlar':['hamsa','devon','gazal']
#                 }
# tayson = {
#         'ism':'Tayson',
#         't_yil':1960,
#         'y_joy':'new york',
#         'asarlar':['luis', 'kilichko', 'koko']
#         }
# jekichang = {
#             'ism':'jeki chang',
#             't_yil':1965,
#             'y_joy':'pekin',
#             'asarlar':['pol hangomasi', 'kungfu' , 'kobra']
#             }
# mashhurlar = [Alisher_Navoiy, tayson, jekichang]

# for mashhur in mashhurlar:
#     ism = mashhur['ism']
#     asarlar = mashhur['asarlar']
#     print(f"\n{ism.title()}ning quyidagi mashhur ishlari:")
#     for asar in asarlar:
#         print(asar.upper())


# navoiy = {
#         'ism':'alisher navoiy',
#         'asarlar':["Hamsa", "Doston","Devon"]
#     }

# tayson = {
#         'ism':'mayk tayson',
#         'asarlar':["luis","kilichko","koko"]    
#     }
# jeki = {
#         'ism':'jeki chang',    
#         'asarlar':["hangoma","komediya","taruxiy"]
#         }
# mashhurlar = [navoiy,tayson,jeki]
# for mashhur in mashhurlar:
#     ism = mashhur['ism']
#     asarlar = mashhur['asarlar']
#     print(f"\n{ism.title()}ning mashhur ishlari")
#     for asar in asarlar:
#         print(asar)







# for mashhur in mashhurlar:
#     print(f"{mashhur['ism'].title()}, "
#           f"{mashhur['t_yil']} yilda tugilgan, "
#           f"{mashhur['y_joy']} shahrida yashaydi")       
# yaqinlarim = {
#     'otam':['vatan', 'oila','sadoqat'],
#     'ayam':['guzallik','yoz ifori','hovli'],
#     'dostim':['komediya','tarixiy','dramma']
#     }
# for ism,kinolar in yaqinlarim.items():
#     print(f"\n{ism.title()}ning sevimli kinolari")
#     for kino in kinolar:
#         print(kino)



# davlatlar = {
#     'uzbekistan':{
#         'poytaxti':'toshkent',
#         'tili':'uzbek tili', 
#         'millati':'uzbek'
#         },   
#     'rossiya':{
#         'poytaxti':'moskiva',
#         'tili':'rus tili', 
#         'millati':'rus'
#         },
#     'xitoy':{
#         'poytaxti':'pekin',
#         'tili':'xitoy tili', 
#         'millati':'xitoy'
#         }
#     }
# davlat = input('Davlat nomini kiriting:>>>  ').lower()

# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n {davlat.title()}ning poytaxti {info['poytaxti'].title()}"
#           f"\n Tili \: {info['tili']}"
#           f"\n Millati: {info['millati']}")
# else:
#      print('Bizda bunday davlat haqida malumot yoq')
    
    
    
    
# for davlat, info in davlatlar.items():
#     print(f"\n {davlat.title()}ning poytaxti {info['poytaxti'].title()}"
#           f"\n Tili \: {info['tili']}"
#           f"\n Millati: {info['millati']}")





























