import requests

def send_alert(message, telegram_bot_token, telegram_chat_id):
    """
    Отправка предупреждения в Telegram группу.
    :param message: Текст сообщения.
    :param telegram_bot_token: Токен Telegram бота.
    :param telegram_chat_id: ID чата или канала.
    """
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {
        'chat_id': telegram_chat_id,
        'text': message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Ошибка при отправке сообщения: {response.text}")
        else:
            print("Сообщение успешно отправлено в Telegram.")
    except Exception as e:
        print(f"Исключение при отправке сообщения в Telegram: {e}")
