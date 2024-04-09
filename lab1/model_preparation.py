"""
Скрипт создает и обучает модель машинного обучения на подготовленных данных из папки train.
При обучении модели используется библиотека CatBoostRegressor.
Результат обучения модели сохраняется в файл model.pkl в директории model.
"""
import argparse
import os
import pickle
import pandas as pd

from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error


def read_data(data_path: str) -> pd.DataFrame:
    """
    Читает данные из csv файла
    :param data_path: путь к файлу
    :return: pd.DataFrame
    """
    data = pd.read_csv(data_path)
    return data


def split_data(data: pd.DataFrame, target: str) -> (pd.DataFrame, pd.Series):
    """
    Разделяет данные на фичи и целевую переменную
    :param data: pd.DataFrame
    :return: pd.DataFrame, pd.Series
    """
    X = data.drop(columns=[target])
    y = data[target]
    return X, y


def train_model(X: pd.DataFrame, y: pd.Series) -> CatBoostRegressor:
    """
    Обучает модель на данных
    :param X: pd.DataFrame
    :param y: pd.Series
    :return: CatBoostRegressor
    """
    model = CatBoostRegressor(iterations=100, depth=5, learning_rate=0.1, loss_function='RMSE', verbose=0)
    model.fit(X, y)
    return model


def save_model(model: CatBoostRegressor, model_path: str, model_file_name: str) -> None:
    """
    Сохраняет модель в файл
    :param model: CatBoostRegressor
    :param model_path: путь к файлу
    :param model_file_name: имя файла
    """
    for path in [args.model_path]:
        os.makedirs(path, exist_ok=True)
    with open(os.path.join(model_path, model_file_name), 'wb') as file:
        pickle.dump(model, file)


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description='Model training')
    parser.add_argument('--test_data_path', type=str, default="test/", help='Path to save test data')
    parser.add_argument('--train_data_path', type=str, default="train/", help='Path to save train data')
    parser.add_argument('--prepared_train_file_name', type=str, default="prepared_train.csv", help='Name of the '
                                                                                                   'prepared train file')
    parser.add_argument('--prepared_test_file_name', type=str, default="prepared_test.csv", help='Name of the '
                                                                                                   'prepared test file')
    parser.add_argument('--target_variable', type=str, default='rhum', help='Name of the target variable')
    parser.add_argument('--model_path', type=str, default="model/", help='Path to save the model')
    parser.add_argument('--model_file_name', type=str, default="model.pkl", help='Name of the model file')

    # Simulate command line arguments
    #argv = ['--target_variable', 'rhum']
    #args = parser.parse_args(argv)

    args = parser.parse_args()

    # Load data
    train = read_data(os.path.join(args.train_data_path, args.prepared_train_file_name))

    # Split data
    X_train, y_train = split_data(train, args.target_variable)

    # Train model
    model = train_model(X_train, y_train)

    # Save model
    save_model(model, args.model_path, args.model_file_name)

    print(f"Model is trained and saved to {args.model_path}/{args.model_file_name}")
