"""Данный скрипт выкачивает данные реальных погодных наблюдений. В качестве параметров принимает:
- дату начала и конца периода наблюдений,
- географические координаты места наблюдений.
"""
import os

import pandas as pd
import argparse

from meteostat import Point, Hourly
from datetime import datetime
from typing import Optional, Tuple

from sklearn.model_selection import train_test_split


def get_weather_data(lat: float, lon: float, alt: Optional[float], start_date: datetime,
                     end_date: datetime) -> pd.DataFrame:
    """
    Get weather data for the specified location in the specified period
    :param lat: Latitude of the location
    :param lon: Longitude of the location
    :param alt: Altitude of the location (optional)
    :param start_date: Beginning of the period
    :param end_date: End of the period
    :return: DataFrame with weather data
    """
    # Create Point
    location = Point(lat, lon, alt)
    # Get hourly data
    hourly = Hourly(location, start_date, end_date)
    hourly = pd.DataFrame(hourly.fetch())
    # Delete columns with missing values
    hourly = hourly.dropna(axis=1, how='any')
    return hourly


# Функция разделения данных на обучающую и тестовую выборки
def split_data(data: pd.DataFrame, test_size: float = 0.3) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split data into training and test sets
    :param data: DataFrame with data
    :param test_size: The proportion of the dataset to include in the test split
    :return: Training and test sets
    """
    # Split data
    train, test = train_test_split(data, test_size=test_size, shuffle=False)
    return train, test


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description='Download weather data')
    parser.add_argument('--test_data_path', type=str, default="test/", help='Path to save test data')
    parser.add_argument('--origin_test_file_name', type=str, default="test.csv", help='Name of the original test file')
    parser.add_argument('--train_data_path', type=str, default="train/", help='Path to save train data')
    parser.add_argument('--origin_train_file_name', type=str, default="train.csv", help='Name of the original train '
                                                                                        'file')
    parser.add_argument('--lat', type=float, required=True, help='Latitude of the location (ie. 7.8804)')
    parser.add_argument('--lon', type=float, required=True, help='Longitude of the location (ie. 98.3923')
    parser.add_argument('--alt', type=float, help='Altitude of the location (ie. 10.0)')
    parser.add_argument('--start_date', type=str, required=True, help='Beginning of the period (ie. 2020-01-01 '
                                                                      '00:00:00)')
    parser.add_argument('--end_date', type=str, required=True, help='End of the period (ie. 2020-12-31 23:00:00)')

    # Simulate command line arguments
    #argv = ['--lat', '7.8804', '--lon', '98.3923', '--alt', '10.0', '--start_date', '2020-01-01 00:00:00', '--end_date', '2020-1-31 23:00:00']
    #args = parser.parse_args(argv)

    args = parser.parse_args()

    # Convert dates to datetime
    start_date = datetime.strptime(args.start_date, '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(args.end_date, '%Y-%m-%d %H:%M:%S')

    # Get weather data
    data = get_weather_data(args.lat, args.lon, args.alt, start_date, end_date)

    # Split data
    train, test = split_data(data)

    # Save data
    for path in [args.train_data_path, args.test_data_path]:
        os.makedirs(path, exist_ok=True)
    train_path = os.path.join(args.train_data_path, args.origin_train_file_name)
    test_path = os.path.join(args.test_data_path, args.origin_test_file_name)
    train.to_csv(train_path, index=False)
    test.to_csv(test_path, index=False)
    print(f"Data saved successfully to {train_path} and {test_path}")
