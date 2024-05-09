"""
Модуль для работы с моделью:
    - обучение модели
    - сохранение модели
    - загрузка модели
    - предсказание
"""

import os
import pickle
from catboost import CatBoostClassifier

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


# Класс для работы с моделью
class Model:
    def __init__(self):
        self.model = CatBoostClassifier(iterations=100, learning_rate=0.5, depth=10, loss_function='MultiClass')
        logger.info('Model object created')

    def fit(self, X_train, y_train) -> None:
        self.model.fit(X_train, y_train)
        logger.info('Model fitted')

    def evaluate(self, X_test, y_test) -> float:
        logger.info(f'Model score: {self.model.score(X_test, y_test)}')
        return self.model.score(X_test, y_test)

    def save(self, score) -> str:
        os.makedirs(os.path.join(DATA_DIR, 'model'), exist_ok=True)
        with open(os.path.join(DATA_DIR, f'model/iris_model_{score}.pkl'), 'wb') as file:
            pickle.dump(self.model, file)
        logger.info('Model saved')

        return os.path.join(DATA_DIR, f'model/iris_model_{score}.pkl')

    def load(self):
        with open(os.path.join(DATA_DIR, 'model/iris_model.pkl'), 'rb') as file:
            self.model = pickle.load(file)
        logger.info('Model loaded')

    def predict(self, X):
        return self.model.predict(X)

    def get_feature_importance(self):
        return self.model.get_feature_importance()
