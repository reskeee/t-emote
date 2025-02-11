import uuid
import os
import time
import telebot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def hello(message):
    bot.reply_to(message, "Hello")


@bot.message_handler(content_types=["audio", 'document'])
def getfile(message):
    if message.content_type == 'document':  # wav
        file = bot.get_file(message.document.file_id)
    elif message.content_type == 'audio':  # mp3
        file = bot.get_file(message.audio.file_id)
    download_file = bot.download_file(file.file_path)
    file_name = str(uuid.uuid4()) + ".wav"

    with open(f"storage/{file_name}", "wb") as new_file:
        new_file.write(download_file)

    bot.reply_to(message, "Файл скачан")
    result = processfile(file_name)
    bot.reply_to(message, result)


def processfile(file_name):
    time.sleep(10)
    return "wait"


if __name__ == "__main__":
    bot.infinity_polling()
