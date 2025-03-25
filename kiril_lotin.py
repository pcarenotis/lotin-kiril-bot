import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = '7766858721:AAFQ0-xK_9jGvYviSureq0jRQHFqEtBMlK8'
ADMIN_ID = 1998362597  # O‘zingizning Telegram ID'ingizni yozing

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Matn kiriting")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    matn = message.text
    javob = to_cyrillic(matn) if matn.isascii() else to_latin(matn)
    
    # Foydalanuvchiga javob yuborish
    bot.reply_to(message, javob)
    
    # Xabarni admin-ga yuborish
    user_info = f"👤 @{message.from_user.username} (ID: {message.from_user.id})" if message.from_user.username else f"👤 ID: {message.from_user.id}"
    admin_message = f"📩 Yangi xabar:\n{user_info}\n💬 {matn}"
    
    bot.send_message(ADMIN_ID, admin_message)  # Admin-ga xabar yuborish

bot.infinity_polling()
