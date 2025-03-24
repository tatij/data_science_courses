# Файл визуализации и обработки выбросов датасета (mdl_outliers.py)
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import zscore

# Поиск и удаление выбросов
def outliers_data(dataset, columns):
  try:
    for column in columns:
      # Z-оценка
      # Вычисление Z-оценка
      dataset['z_score'] = zscore(dataset[column])

      # Определение выбросов
      threshold = 3
      outliers = dataset[(dataset['z_score'] > threshold) | (dataset['z_score'] < -threshold)]

      # Подсчет количества выбросов
      num_outliers = outliers.shape[0]
      print(f'Всего {column} выбросов: {num_outliers} ')

      # Удаление выбросов
      df_cleaned = dataset[(dataset['z_score'] <= threshold) & (dataset['z_score'] >= -threshold)]

      # Удаление временный столбец z_score
      df_cleaned = df_cleaned.drop(columns=['z_score'])      

    print(f'Всего: {len(df_cleaned)}')
    print(df_cleaned.describe())

    return df_cleaned
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)


        