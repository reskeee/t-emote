from mistralai import Mistral
import requests
import numpy as np
import os
from getpass import getpass

api_key='f3WKj0XVDzMHTngqMzf5DyAydVq1W696'
client = Mistral(api_key=api_key)

model = "mistral-large-latest"


def get_emo(sentence):
    chat_response = client.chat.complete(
        model= model,
        messages = [
            {
                "role": "system",
                "content": "Твоя задача - классификация предложений по эмоциям, которые они выражают. Всего предложения можно разбить на 4 класса: neutral - нейтральная окраска, angy - предложения, в которых выражается злость или агрессия, sad - предложения, в которых выражается грусть, happy - предложения, в которых выражается радость. Когда на вход подается сообщение, нужно вывести только 1 слово - класс, определенный после анализа предложения."
            },
            {
                "role": "user",
                "content": sentence
            }
        ]
    )

    return chat_response.choices[0].message.content

# print(chat_response.choices[0].message.content)
