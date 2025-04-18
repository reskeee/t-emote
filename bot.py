import uuid
import os
import telebot
from dotenv import load_dotenv
from ai_module import get_audio_start, get_audio_end, get_text_emo, get_audio_emo, model

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def hello(message):
    bot.reply_to(message, "Привет, я бот-определиттель эмоций. Отправь мне аудиофайл и я скажу, какие эмоции испытывает говорящий человек")


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
    trascribe = model.transcribe(f"storage/{file_name}")['text']
    # print(trascribe)
    text_res = get_text_emo(trascribe)
    audio_res = get_audio_emo(f"storage/{file_name}")

    response = f"Эмоция по тексту: {text_res}\nЭмоция по аудио: {audio_res}"

    print(trascribe)

    return response


if __name__ == "__main__":
    # bot.infinity_polling()

    processfile("storage/call.mp3")
