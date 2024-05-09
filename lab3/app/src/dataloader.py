"""
Обработчик данны:
    - загрузка данных из источника
    - преобразование данных
    - сохранение данных
"""

import os
import pandas as pd
from sklearn.datasets import load_iris

from logging import getLogger

# Инициализируем и сконфигурируем логгер, чтобы он стримил логи в stdout с временем выполнения
logger = getLogger(__name__)
logger.setLevel('INFO')
from logging import StreamHandler
handler = StreamHandler()
handler.setLevel('INFO')
from logging import Formatter
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Определяем путь к директории с данными
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


# Класс для загрузки данных
class DataLoader:
    def __init__(self):
        self.iris = load_iris()
        self.iris_df = pd.DataFrame(self.iris.data, columns=self.iris.feature_names)
        self.iris_df['target'] = self.iris.target

    def save_dataset(self):
        # Создаем директорию для датасетов
        os.makedirs(os.path.join(DATA_DIR, 'datasets'), exist_ok=True)
        logger.info('Создана директория для датасетов')
        # Записываем датасет в CSV
        self.iris_df.to_csv(os.path.join(DATA_DIR, 'datasets/iris_dataset.csv'), index=False)
        logger.info('Датасет сохранен в CSV')

    def load_dataset(self):
        return pd.read_csv(os.path.join(DATA_DIR, 'datasets/iris_dataset.csv'))

    def get_data(self):
        return self.iris.data

    def get_target(self):
        return self.iris.target

    def get_feature_names(self):
        return self.iris.feature_names

    def get_class_names(self):
        return {i: name for i, name in enumerate(self.iris.target_names)}

    def get_class_name(self, class_index):
        return self.iris.target_names[class_index]


# Класс для предобработки данных
class DataPreprocessor:
    def __init__(self):
        self.data_loader = DataLoader()
        self.X = self.data_loader.get_data()
        self.y = self.data_loader.get_target()

    def preprocess(self):
        # Выполняем пред обработку данных
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler

        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        logger.info('Данные разделены на обучающую и тестовую выборки')
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        logger.info('Данные масштабированы')

        return X_train_scaled, X_test_scaled, y_train, y_test, scaler

    def scale(self, data, scaler):
        return scaler.transform(data)