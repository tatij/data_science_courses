# module_for_laptop.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sys

label_encoder = LabelEncoder();

# загрузка датасета
def load_dataset(file_path, target, test_size = 0.2, random_state = 42 ):
    """
    Загрузка данных из CSV файла.
    :return: dataset с загруженными данными.
    """
    try:    
           dataset = pd.read_csv(file_path)
           dataset.model = LinearRegression()
           dataset.scaler = StandardScaler()

           X = dataset.drop(target, axis=1)  # Все столбцы, кроме target
           y = dataset[target]  # Только столбец target

           # Разделим данные на тренировочную и тестовую выборки
           dataset.X_train, dataset.X_test, dataset.y_train, dataset.y_test = train_test_split(X, y, test_size=0.3, random_state=42)
                
           print("Данные успешно загружены.")
           print("Матрица признаков X:")
           print(X)
     
           print("\nЦелевая переменная y:")
           print(y)

    except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")
            sys.exit(1)
    return dataset

# Кодируем по категориям    
def encoder(dataset, args) -> None:
    for i in args:
        dataset[i + ' (Encoded)'] = label_encoder.fit_transform(dataset[i])

# Подсчет пустых значений
def count_empty_values(dataset):
  print('\nКоличество строк и столбцов')
  print(dataset.shape)
  dataset.describe(include = "all")
  print(dataset.info())
  #mask = dataset['Price ($)'] == dataset.groupby('Group')['Price ($)'].transform('max')
  #max_rows = dataset[mask]
  #print('\nПосмотреть')
  #print(max_rows['Group'])
  #print('\n_________')








