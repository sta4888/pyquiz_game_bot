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

start_message = "Для использования \n\n <b>команды</b>\n\n" \
                "/start - Для начала работы бота\n"

if __name__ == "__main__":
    pass