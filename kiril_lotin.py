import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = '7766858721:AAFQ0-xK_9jGvYviSureq0jRQHFqEtBMlK8'
bot = telebot.TeleBot(TOKEN, parse_mode = None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Matn kiriting")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    matn = message.text
    javob = lambda matn: to_cyrillic(matn) if matn.isascii() else to_latin(matn)
    bot.reply_to(message, javob(matn))
	

bot.infinity_polling()
