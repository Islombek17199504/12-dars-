from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = '1972130351:AAFRNJxI1xnx1IwuDiBqUiebhXM3yKeVhvk'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob  = "Assalomu alaykum"
    javob +="\nMatn kiriting:"
    bot.reply_to(message,javob)


@bot.message_handler(func=lambda message:True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message,javob)

bot.polling()
# matn = input("Matnni kiritng: ")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
    
    