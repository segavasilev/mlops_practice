import pickle

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from .src.dataloader import DataLoader, DataPreprocessor
from .src.model import Model


# Определяем входные параметры модели
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


app = FastAPI()

# Создаем объекты для работы с данными
data_loader = DataLoader()
data_preprocessor = DataPreprocessor()
model = Model()

# Загружаем данные
data_loader.save_dataset()
data_loader.load_dataset()

# Предобрабатываем данные
X_train_scaled, X_test_scaled, y_train, y_test, scaler = data_preprocessor.preprocess()

# Обучаем модель
model.fit(X_train_scaled, y_train)

# Оцениваем качество модели
score = model.evaluate(X_test_scaled, y_test)

# Сохраняем модель
model_path = model.save(score)

app = FastAPI()

# Загружаем модель
model = pickle.load(open(model_path, 'rb'))


# Определяем класс для предсказания
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Определяем роут для предсказания
@app.post("/predict")
def predict(data: IrisInput):
    data = data.dict()  # Convert the input data to a dictionary
    data = pd.DataFrame(data, index=[0])
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)
    # Конвертируем предсказание в название класса
    return {'prediction': data_loader.get_class_name(prediction[0].tolist()[0])}



# Определяем роут для проверки работоспособности
@app.get("/")
def read_root():
    return {"Для предсказания модели необходимо отправить POST запрос со следующим содержимым":

            {"sepal_length": 0.0,
             "sepal_width": 0.0,
             "petal_length": 0.0,
             "petal_width": 0.0},

            "Подробнее о модели можно узнать по адресу": "/docs"
            }


# Определяем роут для проверки работоспособности модели на тестовых данных
@app.get("/test")
def test():
    prediction = model.predict(X_test_scaled)
    return prediction.tolist()


# Определяем роут для проверки качества модели на тестовых данных
@app.get("/score")
def score():
    return score
