import time
import logging
from data_loader import load_historical_data
from model_trainer import train_model, load_trained_model
from api_monitor import fetch_current_data
from alert_notifier import send_alert
import config


def main():
    # Настройка логирования
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Проверка наличия токенов
    if not config.TELEGRAM_BOT_TOKEN or not config.TELEGRAM_CHAT_ID:
        logging.error("Необходимо установить TELEGRAM_BOT_TOKEN и TELEGRAM_CHAT_ID в переменных окружения.")
        return

    # Загрузка и подготовка данных
    historical_data = load_historical_data(config.HISTORICAL_DATA_PATH)
    if historical_data is None:
        logging.error("Не удалось загрузить исторические данные.")
        return

    # Обучение или загрузка модели
    model = None
    try:
        model = load_trained_model(config.FINE_TUNED_MODEL_PATH)
        logging.info("Дообученная модель успешно загружена.")
    except:
        logging.info("Дообученная модель не найдена. Начинается обучение модели.")
        model = train_model(historical_data)
        if model is None:
            logging.error("Не удалось обучить модель.")
            return
        else:
            logging.info("Модель успешно обучена и сохранена.")

    # Основной цикл приложения
    while True:
        # Периодический опрос API
        current_data = fetch_current_data(config.API_URLS)
        if current_data is None:
            logging.warning("Не удалось получить текущие данные. Повторный опрос через некоторое время.")
            time.sleep(config.POLL_INTERVAL)
            continue

        # Прогнозирование вероятности
        probabilities = model.predict(current_data)

        # Проверка порога вероятности
        for index, prob in enumerate(probabilities):
            if prob > config.THRESHOLD:
                city = current_data.iloc[index]['city'] if 'city' in current_data.columns else 'Неизвестный город'
                message = f"Предупреждение для {city}: вероятность эпидемии составляет {prob * 100:.2f}%"
                send_alert(message, config.TELEGRAM_BOT_TOKEN, config.TELEGRAM_CHAT_ID)
                logging.info(f"Отправлено предупреждение для {city}.")

        # Задержка перед следующим опросом
        logging.info("Ожидание перед следующим опросом API.")
        time.sleep(config.POLL_INTERVAL)


if __name__ == '__main__':
    main()
