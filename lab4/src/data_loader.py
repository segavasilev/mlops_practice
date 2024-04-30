from catboost.datasets import titanic

# Загружаем датасет
data_df, _ = titanic()

# Сохраняем в файл
data_df.to_csv('../data/titanic_data.csv', index=False)