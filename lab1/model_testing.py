"""
Скрипт проверяет модель машинного обучения на построенных данных из папки test
"""

import os
import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error

import argparse

from lab1.model_preparation import read_data
from lab1.model_preparation import split_data

def load_model(model_path: str, model_file_name: str) -> object:
    """
    Загружает модель из файла
    :param model_path: путь к файлу
    :param model_file_name: имя файла
    :return: object
    """
    with open(os.path.join(model_path, model_file_name), 'rb') as file:
        model = pickle.load(file)
    return model

def test_model(model: object, X_test: pd.DataFrame, y_test: pd.Series) -> float:
    """
    Проверяет модель на тестовых данных
    :param model: object
    :param X_test: pd.DataFrame
    :param y_test: pd.Series
    :return: float
    """
    y_pred = model.predict(X_test)
    return mean_squared_error(y_test, y_pred)


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description='Model testing')
    parser.add_argument('--test_data_path', type=str, default="test/", help='Path to saved test data')
    parser.add_argument('--prepared_test_file_name', type=str, default="prepared_test.csv", help='Name of the prepared test file')
    parser.add_argument('--model_path', type=str, default="model/", help='Path to saved model')
    parser.add_argument('--model_file_name', type=str, default="model.pkl", help='Name of the model file')
    parser.add_argument('--target_variable', type=str, default='rhum', help='Name of the target variable')

    # Simulate command line arguments
    #argv = ['--target_variable', 'rhum']
    #args = parser.parse_args(argv)

    args = parser.parse_args()

    # Load data
    test = read_data(os.path.join(args.test_data_path, args.origin_test_file_name))

    # Split data
    X_test, y_test = split_data(test, args.target_variable)

    # Load model
    model = load_model(args.model_path, args.model_file_name)

    # Test model
    mse = test_model(model, X_test, y_test)
    print(f'Model test accuracy is: {mse}')