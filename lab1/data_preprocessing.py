"""
Скрипт выполняет предобработку данных путем генерации признаков с заданным лагом.
Поскольку используется CatBoost, предварительное масштабирование признаков не требуется.
Главное требование к данным - отсутствие пропусков.

"""

import pandas as pd
import argparse


# Функция для создания признаков
def create_features(data: pd.DataFrame, target: str, lags: int = 1) -> pd.DataFrame:
    """
    Create features for machine learning
    :param data: DataFrame with data
    :param target: Target variable
    :param lags: Number of lagged values
    :return: DataFrame with features
    """
    # Create lagged values
    for lag in range(1, lags + 1):
        data[f'{target}_lag_{lag}'] = data[target].shift(lag)
    return data


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description='Data preprocessing')
    parser.add_argument('--data', type=list, required=True, help='List of paths to the data files')
    parser.add_argument('--target', type=str, required=True, help='Name of the target variable')
    parser.add_argument('--lags', type=int, default=1, help='Number of lagged values')
    args = parser.parse_args()


