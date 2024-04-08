"""
Скрипт проверяет модель машинного обучения на построенных данных из папки “test”
"""

import os
import pickle
import numpy as np
from sklearn.metrics import mean_squared_error
from logging import getLogger, StreamHandler, INFO

# Путь к папке с данными
DATA_PATH = 'test'

# Путь к файлу модели
MODEL_PATH = 'model.pkl'

# Логирование метрик
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.addHandler(handler)
logger.setLevel(INFO)

# Загрузка модели
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Загрузка данных
for file in os.listdir(DATA_PATH):
    if file.endswith('scaled.npy'):
        test_data = np.load(os.path.join(DATA_PATH, file))

# Разделение данных на признаки и целевую переменную
X_test = test_data[:, :-1]
y_test = test_data[:, -1]

# Предсказание на тестовой выборке
y_pred = model.predict(X_test)

# Оценка качества модели
accuracy = mean_squared_error(y_test, y_pred)
logger.info(f'Model test accuracy is: {accuracy}')

