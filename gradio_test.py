import gradio as gr
from mistral_test import get_emo


# Функция для взаимодействия с языковой моделью
def chat_with_model(user_input):
    # Здесь вы можете добавить логику для отправки запроса к вашей языковой модели
    # и получения ответа. В данном примере мы просто возвращаем введенный текст.
    emo = get_emo(user_input)

    response = f"Распознанная эмоция: {emo}"
    return response


iface = gr.Interface(
    fn=chat_with_model,
    inputs=gr.Textbox(lines=2, placeholder="Введите ваш текст здесь..."),
    outputs=gr.Textbox(lines=2, label="Ответ"),
    title="Интерфейс взаимодействия с языковой моделью",
    description="Введите текст, чтобы получить ответ от языковой модели.",
    # layout="vertical"  # Устанавливаем вертикальное расположение
)

# Запуск интерфейса
iface.launch()
