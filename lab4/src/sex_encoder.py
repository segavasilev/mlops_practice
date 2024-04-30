import pandas as pd

"""Создайте новый признак в датасете lab4/data/titanic_data.csv с использованием one-hot-encoding для строкового признака «Пол» (“Sex”). 
Добавьте признак к исходному датасету и сохраните результат в тот же файл."""

def encode(data):
    data = pd.get_dummies(data, columns=['Sex'], prefix='Sex')
    return data

def main():
    data = pd.read_csv('../data/titanic_data.csv')
    data = encode(data)
    data.to_csv('../data/titanic_data.csv', index=False)

if __name__ == '__main__':
    main()