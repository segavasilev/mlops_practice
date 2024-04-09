#!/bin/bash

# Установим pip3
apt update
apt install python3-pip -y
apt install python3.10-venv -y

# Создадим окружение
python3 -m venv .venv

# Активируем окружение
source .venv/bin/activate

# Устанавливем библиотеки
pip install -r requirements.txt

# Запуск всех скриптов
output_paths=$(python3 data_creation.py --lat 7.8804 --lon 98.3923 --alt 10.0 --start_date "2020-01-01 00:00:00" --end_date "2020-1-31 23:00:00")
echo $output_paths
#python3 data_preprocessing.py
#python3 model_preparation.py
#python3 model_testing.py

# Деактивируем окружение
deactivate