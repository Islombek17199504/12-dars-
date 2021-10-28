
# import random

# from uzwords import words

# def get_word():
#     word = random.choice(words)
    
#     while '-' in word or ' ' in word:
#         word = random.choice(words)
#     return word.upper()

# def display(user_letter,word):
#     display_letter = ""
#     for letter in word:
#         if letter in user_letter.upper():
#             display_letter += letter
#         else:
#             display_letter = "-"
#     return display_letter

# def play():
#     word = get_word()
    
#     word_letters = set(word)
    
#     user_letter = ''
    
#     print(f"Men {len(word)} xonali sz o'yladim")
    
#     while len(word_letters)>0:
#         print(display(user_letter, word))
#         if len(user_letter)>0:
#             print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letter}")
            
#         letter = input("Harf kiritng: ").upper()
#         if letter in user_letter:
#             print("Bu harfni avval kiritgansiz. Boshqa harf kiritng.")
#             continue
#         elif letter in word:
#             word_letters.remove(letter)
#             print(f"{letter} harfi to'g'ri")
#         else:
#             print(f"Bunday harf yo'q")
#         user_letter += letter
#     print(f"Tabriklayman {word} so'zni {len(user_letter)} ta urinishda topdingiz")