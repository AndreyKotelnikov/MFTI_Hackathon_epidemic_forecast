import os

# Настройки приложения
HISTORICAL_DATA_PATH = 'data/historical_data.csv'
PRE_TRAINED_MODEL_PATH = 'models/pre_trained_model.h5'
FINE_TUNED_MODEL_PATH = 'models/fine_tuned_model.h5'
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
THRESHOLD = 0.8  # Порог вероятности для отправки предупреждения
POLL_INTERVAL = 3600  # Интервал опроса API в секундах (1 час)
API_URLS = [
    'https://api.monitoringcenter1.ru/current_data',
    'https://api.monitoringcenter2.ru/current_data',
    # Добавьте остальные URL API
]
