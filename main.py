import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

bot.set_my_commands([
    telebot.types.BotCommand("/start", "Для начала работы"),
    telebot.types.BotCommand("/help", "Инструкция использования"),
])

start_message = "<b>команды</b> Для использования\n\n" \
                "/start - Для начала работы бота\n" \
                "/help - Помощь в использовании"


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = int(message.chat.id)
    bot.send_message(chat_id, f"Привет")


@bot.message_handler(commands=['help'])
def help_method(message):
    chat_id = int(message.chat.id)
    bot.send_message(chat_id, f"{start_message}", parse_mode='html')


if __name__ == "__main__":
    bot.polling(none_stop=True)
