"""
Скрипт выполняет предобработку данных путем генерации признаков с заданным лагом.
Поскольку используется CatBoost, предварительное масштабирование признаков не требуется.
Главное требование к данным - отсутствие пропусков.

"""

import os

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
    parser.add_argument('--test_data_path', type=str, default="test/", help='Path to save test data')
    parser.add_argument('--origin_test_file_name', type=str, default="test.csv", help='Name of the original test file')
    parser.add_argument('--train_data_path', type=str, default="train/", help='Path to save train data')
    parser.add_argument('--origin_train_file_name', type=str, default="train.csv", help='Name of the original train '
                                                                                        'file')
    parser.add_argument('--prepared_train_file_name', type=str, default="prepared_train.csv", help='Name of the '
                                                                                                   'prepared train file')
    parser.add_argument('--prepared_test_file_name', type=str, default="prepared_test.csv", help='Name of the '
                                                                                                 'prepared test file')
    parser.add_argument('--prepared_test_file_name', type=str, default="prepared_test.csv", help='Name of the '
                                                                                                 'prepared test file')
    parser.add_argument('--target_variable', type=str, default='rhum', help='Name of the target variable')

    args = parser.parse_args()

    # Load data
    train = pd.read_csv(os.path.join(args.train_data_path, args.origin_train_file_name))
    test = pd.read_csv(os.path.join(args.test_data_path, args.origin_test_file_name))

    # Create features
    train = create_features(train, args.target_variable)
    test = create_features(test, args.target_variable)

    # Save prepared data
    train.to_csv(os.path.join(args.train_data_path, args.prepared_train_file_name), index=False)
    test.to_csv(os.path.join(args.test_data_path, args.prepared_test_file_name), index=False)

    print(f'Data preprocessing is finished. '
          f'Prepared train data saved to {args.train_data_path}/{args.prepared_train_file_name}'
          f' and prepared test data saved to {args.test_data_path}/{args.prepared_test_file_name}')
