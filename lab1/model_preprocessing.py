"""
Скрипт выполняет предобработку данных с помощью sklearn.preprocessing.StandardScaler.
Трансформации выполняются и над тестовой и над обучающей выборкой.
Результаты сохраняются в папки “train” и “test” в формате .npy.
"""

import numpy as np
from sklearn.preprocessing import StandardScaler
import os


def main():
    # Загрузка данных
    train_data = np.load('train/train_data.npy')
    test_data = np.load('test/test_data.npy')

    # Применение StandardScaler к второму столбцу
    scaler = StandardScaler()
    train_data[:, 1:] = scaler.fit_transform(train_data[:, 1:])
    test_data[:, 1:] = scaler.transform(test_data[:, 1:])

    # Сохранение результатов
    np.save('train/train_data_scaled', train_data)
    np.save('test/test_data_scaled', test_data)


if __name__ == '__main__':
    main()
