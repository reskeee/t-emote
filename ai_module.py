import whisper
from moviepy.editor import AudioFileClip
from langchain_gigachat.chat_models import GigaChat
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage
from typing import Dict
import gigaam
from convert import convert_to_wav

load_dotenv()

model = whisper.load_model("base")  # Доступные модели: tiny, base, small, medium, large
model_giga = GigaChat(
    credentials=os.getenv('CREDENTIALS'),
    scope=os.getenv('SCOPE'),
    model=os.getenv('MODEL'),
    verify_ssl_certs=False
)
model_gigaam = gigaam.load_model('emo')


def get_audio_start(filename):
    audio = AudioFileClip(filename)
    start = audio.subclip(0, 20)
    start.write_audiofile("start.mp3")


def get_audio_end(filename):
    audio = AudioFileClip(filename)
    length = int(audio.duration)
    end = audio.subclip(length - 20, length)
    end.write_audiofile('end.mp3')


def get_text_emo(text):
    true_text = text['text']
    print(true_text)
    task = f"Сейчас я отправлю тебе разговор между двумя людьми. {true_text}. Проанализируй его и назови эмоцию, которую испытывают его участники одним словом, например: веселье, злость, грусть. В ответ отправь только слово, описывающее эмоцию разговора"
    messages = [HumanMessage(content=task)]
    response = model_giga.invoke(messages)
    return response.content


def get_audio_emo(filepath) -> str:
    emotion2prob: Dict[str, int] = model.get_probs(filepath)
    return sorted(list(emotion2prob.items()), key=lambda x: x[1], reverse=True)[0][0]

# print(mood(start_result))
# print(mood(end_result))
# start_result = model.transcribe("GigaAM/test/ex.wav")
# end_result = model.transcribe("end.mp3")

# print(start_result)