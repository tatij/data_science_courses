# Файл анализа датасета (mdl_analysis.py)
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sys.path.append('/content/sample_data')
import mdl_visualization as visual

# Вывод статистической информации
def statistic_data(dataset):
  try:
    # Загрузка  данных и просмотр первых 5 записей
    print("First 5 records:", dataset.head())

    # Информация о типах данных
    print(dataset.info())

    # Статистическая информация
    print(dataset.describe())

    # Проверка на пропущенные значения
    print(dataset.isnull().sum())
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Анализ данных
def analysis_data(dataset):
  try:  
    # Вычисление количества нулевых значений и % от общего числа 
    zero = 0
    count_all = len(dataset)    
    columns = ['price', 'level', 'levels', 'rooms', 'kitchen_area']
    for column in columns:
      count_zero = (dataset[column] <= zero).sum()
      print(f'{column} <= 0 : {count_zero}')
      percent_zero = round(count_zero/count_all*100, 5)
      print(f'% {column} <= 0 : {percent_zero}%')    
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1) 

# Корреляционный анализ
def corr_data(dataset):
  try:        
    correlation_matrix = dataset.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix.T, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Корреляционная Матрица')
    plt.show()
    name_file = 'correlation_matrix.png'
    visual.save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)



