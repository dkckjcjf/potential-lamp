
import telebot

# Укажите токен вашего бота, полученный от BotFather
TOKEN = '8415064614:AAHZeLTseqkYn5bLXV0XAkScYIxe7IlqUeY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("Запускаем бота...")
    bot.polling()
