# Файл предобработки датасета (mdl_preprocessing.py)
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Предобработка датасета с реккомендациями
def preprocessing_data_recommend(dataset):
  try:
    # Уменьшение размерности данных, удаление не нужных столбцов
    dataset = dataset.drop(['postal_code', 'street_id', 'id_region', 'house_id'], axis=1)

    # Удаление нулевых цен
    dataset = dataset[(dataset['price'] > 0)]

    # Удаление площадей кухни -100, т.к. не понимая что это за категория
    dataset = dataset[(dataset['kitchen_area'] >= 0)]

    # Удаляем нулевые значения этажей и этажности
    dataset = dataset[(dataset['level'] > 0) & (dataset['levels'] > 0)]

    # Замена нулевых значений кухни на среднее
    mean_value = round(dataset['kitchen_area'][dataset['kitchen_area'] > 0].mean(), 1)
    dataset.loc[dataset['kitchen_area'] == 0, 'kitchen_area'] = mean_value

    # Преобразование даты в формат datetime
    dataset['date'] = pd.to_datetime(dataset['date'])

    # Проверка предобработки
    print(f'Всего: {len(dataset)}')
    print(dataset.describe())
    print(dataset.info())
        
    return dataset
  except FileNotFoundError as e:
    print(f"Ошибка при загрузке данных: {e}")
    sys.exit(1)

# Предобработка датасета
def preprocessing_data(dataset):
  try:
    # Уменьшение размерности данных, удаление не нужных столбцов
    dataset = dataset.drop(['postal_code', 'street_id', 'house_id'], axis=1)

    # Берем диапазон цен от 20000$ до 120000$
    dataset = dataset[(dataset['price'] <= 10000000) & (dataset['price'] > 1600000)]

    # Удаляем нулевые значения этажей и этажности
    dataset = dataset[(dataset['level'] > 0) & (dataset['levels'] > 0)]

    # Замена нулевых и отрицательных значений кухни на среднее
    mean_value = round(dataset['kitchen_area'][dataset['kitchen_area'] > 0].mean(), 1)
    dataset.loc[dataset['kitchen_area'] <= 0, 'kitchen_area'] = mean_value

    # Замена нулевых и отрицательных значений комнат на среднее значения по площади 
    count_rooms = 1
    area = 0
    while count_rooms <= 9: 
      mean_area = round(dataset['area'][dataset['rooms'] == count_rooms].mean(), 1) 
      if(count_rooms < 9):
        dataset.loc[(dataset['rooms'] <= 0) & (dataset['area'] > area) & (dataset['area'] <= mean_area), 'rooms'] = count_rooms
        area = mean_area
      else:
        dataset.loc[(dataset['rooms'] <= 0) & (dataset['area'] >= area), 'rooms'] = count_rooms
      count_rooms += 1  # Увеличиваем счетчик на 1

    # Преобразование даты в формат datetime
    dataset['date'] = pd.to_datetime(dataset['date'])

    # Проверка предобработки
    print(f'Всего: {len(dataset)}')
    print(dataset.describe())
    print(dataset.info())
        
    return dataset
  except FileNotFoundError as e:
    print(f"Ошибка при загрузке данных: {e}")
    sys.exit(1)

# Преобразование даты в int
def transform_date_to_int(dataset, column):
  try:
    # Преобразование типа object в int64
    if dataset[column].dtypes == 'object':      
      dataset[column] = pd.to_datetime(dataset[column])
      dataset[column] = dataset['date'].astype('int64') // 10**9 
    else:
      dataset[column] = dataset['date'].astype('int64') // 10**9 
    return dataset
    
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Выборка n записей
def sample_data(dataset, sample_size, rs):
  try:      
    dataset = dataset.sample(n=sample_size, random_state=rs) 
    print(dataset.describe())
    return dataset
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

