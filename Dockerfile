# Используем официальный базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем зависимости
COPY requirements.txt .

# Обновляем pip до последней версии (опционально)
RUN pip install --upgrade pip

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY src/ ./src/
COPY data/ ./data/
COPY models/ ./models/

# Копируем файл с переменными окружения (если используется)
COPY .env ./

# Устанавливаем переменные окружения (рекомендуется использовать файл .env)
ENV TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
ENV TELEGRAM_CHAT_ID=${TELEGRAM_CHAT_ID}

# Команда для запуска приложения
CMD ["python", "src/main.py"]
