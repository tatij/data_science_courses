# Файл предобработки датасета (mdl_preprocessing.py)
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Уменьшение размерности данных
def drop_columns(dataset, columns):
  try:
    dataset = dataset.drop(columns, axis=1)        
    return dataset
  except FileNotFoundError as e:
    print(f"Ошибка при загрузке данных: {e}")
    sys.exit(1)

# Преобразование даты
def transform_date(dataset, column):
  try:
    dataset[column] = pd.to_datetime(dataset[column])
    dataset['date_int'] = dataset[column].astype('int64') // 10**9
    print(dataset.info())
    return dataset    
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Выборка периода
def period_date(dataset, target, start, end):
  try: 
    dataset_period = dataset[['Date', target]] 
    dataset_period = dataset_period[(dataset_period['Date'] >= start) & (dataset_period['Date'] < end)]
    dataset_period.set_index('Date', inplace=True)
    print(dataset_period[:10])    
    print(dataset_period.describe())
    return dataset_period
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Дифференцирование данных
def diff_data(dataset):
  try: 
    data_diff = dataset.diff().dropna()
    return data_diff
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

