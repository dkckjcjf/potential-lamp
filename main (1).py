import telebot
from random import choice

# Ваш API-токен, полученный от @BotFather
TOKEN = '8415064614:AAHZeLTseqkYn5bLXV0XAkScYIxe7IlqUeY'

# Список простеньких шуток
jokes = [
    'Ну ты даёшь, друг! Ты меня смеешь!',
    'Я видел твоё сообщение, оно просто огонь!',
    'Держись крепче, это было круто!',
    'Это сообщение заставило мой мозг смеяться!',
    'Так держать, вот это уровень!',
    'От тебя зависит настроение группы!'
]

bot = telebot.TeleBot(TOKEN)

# Обработчик сообщений
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.chat.type in ['group', 'supergroup']:
        # Формируем шутливое сообщение
        response = f"Я Кент коли мельника. {choice(jokes)}"
        
        # Отправляем сообщение обратно в чат
        bot.reply_to(message, response)

if __name__ == "__main__":
    try:
        print("Запускаю бота...")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

