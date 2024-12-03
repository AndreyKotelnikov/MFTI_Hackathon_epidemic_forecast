import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam


def load_trained_model(model_path):
    """
    Загрузка обученной модели.
    :param model_path: Путь к файлу модели.
    :return: Загруженная модель.
    """
    model = load_model(model_path)
    return model


def train_model(data):
    """
    Дообучение предобученной модели на исторических данных.
    :param data: DataFrame с подготовленными историческими данными.
    :return: Обученная модель.
    """
    # Проверка наличия данных
    if data is None:
        print("Ошибка: Данные не загружены.")
        return None

    # Предполагаем, что целевая переменная называется 'epidemic'
    if 'epidemic' not in data.columns:
        print("Ошибка: Целевая переменная 'epidemic' отсутствует в данных.")
        return None

    # Разделение данных на признаки (X) и целевую переменную (y)
    X = data.drop('epidemic', axis=1)
    y = data['epidemic']

    # Разделение на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    try:
        # Загрузка предобученной модели
        model = load_model('models/pre_trained_model.h5')
    except Exception as e:
        print(f"Ошибка при загрузке предобученной модели: {e}")
        return None

    # Компиляция модели
    model.compile(optimizer=Adam(lr=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

    # Дообучение модели
    early_stopping = EarlyStopping(monitor='val_loss', patience=3)
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, callbacks=[early_stopping], batch_size=32)

    # Оценка модели
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Точность модели на тестовых данных: {accuracy * 100:.2f}%")

    # Сохранение дообученной модели
    model.save('models/fine_tuned_model.h5')

    return model
