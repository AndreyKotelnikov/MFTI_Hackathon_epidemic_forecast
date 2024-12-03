import pandas as pd


def load_historical_data(file_path):
    """
    Загрузка и предобработка исторических данных о заболеваниях и эпидемиях в России.
    :param file_path: Путь к CSV файлу с данными.
    :return: DataFrame с подготовленными данными.
    """
    try:
        # Чтение CSV файла
        data = pd.read_csv(file_path)

        # Предобработка данных (заполнение пропусков, кодирование категориальных переменных и т.д.)
        # Например:
        # data.fillna(method='ffill', inplace=True)
        # data = pd.get_dummies(data)

        return data
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None
