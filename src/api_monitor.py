import requests
import pandas as pd


def fetch_current_data(api_urls):
    """
    Запрос текущих данных с API мониторинговых центров городов России.
    :param api_urls: Список URL API для опроса.
    :return: DataFrame с текущими данными.
    """
    data_list = []
    for url in api_urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                # Предполагаем, что данные приходят в формате, совместимом с DataFrame
                data_list.append(data)
            else:
                print(f"Ошибка {response.status_code} при обращении к {url}")
        except Exception as e:
            print(f"Исключение при обращении к {url}: {e}")

    if data_list:
        # Объединение данных в один DataFrame
        current_data = pd.DataFrame(data_list)
        # Предобработка текущих данных (если необходимо)
        # ...
        return current_data
    else:
        print("Не удалось получить текущие данные.")
        return None
