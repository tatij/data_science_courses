# Файл анализа датасета (mdl_analysis.py)
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
sys.path.append('/content/sample_data')
#import mdl_visualization as visual

# Вывод статистической информации
def statistic_data(dataset):
  try:
    # Просмотр первых 5 записей
    print("Первые 5 записей:\n", dataset.head())

    # Просмотр последних 5 записей
    print("\nПоследние 5 записей:\n", dataset.tail())

    # Информация о типах данных
    print("\nТипы данных:\n")
    print(dataset.info())

    # Статистическая информация
    print("\nСтатистическая информация:\n", dataset.describe())

    # Проверка на пропущенные значения
    print("\nПропущенные значения:\n", dataset.isnull().sum())
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Анализ данных
def visual_by_feature(dataset, column):
  try:
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.histplot(dataset[column], kde=True, bins=123, color='blue')
    plt.title(f'Распределение по {column}')
    plt.xlabel(column)
    plt.ylabel('Количество')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    #name_file = f'visual_by_{column}.png'
    #save_plot(fig, name_file)
    plt.show()
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)


