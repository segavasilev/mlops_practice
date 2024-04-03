"""
Скрипт создает и обучает модель машинного обучения на построенных данных из папки “train”.
При обучении модели используется библиотека CatBoostRegressor.
В качестве данных используется предобработанный набор из папки “train” с расширением npz.
Результат обучения модели сохраняется в файл “model.pkl”.
"""

import os
import pickle
import numpy as np
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from logging import getLogger, StreamHandler, INFO

# Путь к папке с данными
DATA_PATH = 'train'

# Путь к файлу модели
MODEL_PATH = 'model/model.pkl'

# Логирование метрик
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.addHandler(handler)
logger.setLevel(INFO)

# Загрузка данных
for file in os.listdir(DATA_PATH):
    if file.endswith('scaled.npy'):
        train_data = np.load(os.path.join(DATA_PATH, file))

# Разделение данных на признаки и целевую переменную
X = train_data[:, :-1]
y = train_data[:, -1]

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение базовой модели
model = CatBoostRegressor(iterations=1000, learning_rate=0.1, depth=10, verbose=100)
model.fit(X_train, y_train)

# Оценка качества модели
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
logger.info(f'Mean Squared Error: {mse}')

# Быстрый файн-тюнинг модели с поиском лучших параметров
model = CatBoostRegressor(iterations=1000, learning_rate=0.1, depth=10, verbose=100)
model.fit(X_train, y_train, eval_set=(X_test, y_test), early_stopping_rounds=50)
logger.info(f'Best iteration: {model.get_best_iteration()}')

# Сохранение модели
with open(MODEL_PATH, 'wb') as file:
    pickle.dump(model, file)
