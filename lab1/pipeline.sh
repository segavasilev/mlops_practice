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
python3 data_creation.py
python3 data_preprocessing.py
python3 model_preparation.py
python3 model_testing.py

# Деактивируем окружение
deactivate