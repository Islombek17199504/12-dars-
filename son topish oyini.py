# print('Hello World')

# import random

# def sontop(x=10):
#     tasodiy_son = random.randint(1, x)
#     print(f"Men 1 dan {x} gacha son o'yladim topa olasizmi")
    
#     while True:
        
#         taxmin = int(input('>>> '))
#         if taxmin< tasodiy_son:
#             print("xato Men o'lagan son bundan kattaroq")
#         elif taxmin > tasodiy_son:
#             print("Xato Men o'lagan son bundan kichikroq")
#         else:
#             break
#     # return taxmin
#     print(f"Tabriklaymiz. Topdiz")
import random


def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    # taxminlar = 0
    while True:
        # taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Kattaroq son ayting:", end="")
        elif taxmin > tasodifiy_son:
            print("Kichikroq son ayting:", end="")
        else:
            print("Yutdingiz!")
            break

    print(f"Tabriklayman ta taxmin bilan topdingiz!")