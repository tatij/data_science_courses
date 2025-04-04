# Файл анализа датасета (mdl_analysis.py)
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
sys.path.append('/content/sample_data')
import mdl_visualization as visual

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

# Корреляционный анализ
def corr_data(dataset):
  try:        
    correlation_matrix = dataset.corr()
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(correlation_matrix.T, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Корреляционная Матрица')
    plt.show()
    name_file = 'correlation_matrix.png'
    visual.save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Тепловая карта
def heat_data(dataset, count):
  try:        
    dataset_heat = dataset.sample(n=count, random_state=42)
    fig, ax = plt.subplots(figsize=(4, 6))
    sns.heatmap(dataset_heat, annot=True, linewidths=.5)
    plt.title('Тепловая карта')
    plt.show()
    name_file = 'heat_map.png'
    visual.save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Тест Дики-Фуллера
def dickey_fuller(dataset, target):
  try:        
    result = adfuller(dataset[target])
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    for key, value in result[4].items():
      print('\t%s: %.3f' % (key, value))
    print(dataset.dtypes)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Метод скользящего среднего (Moving Average) и Экспоненциальное скользящее среднее (ema)
def moving_average(dataset, target, window_size, moving_average, ema):
  try:
    fig, ax = plt.subplots(figsize=(8, 4))    
    plt.plot(dataset.index, dataset[target], label='Исходный ряд')
    plt.plot(moving_average.index, moving_average, label=f'Скользящее среднее ({window_size}-дневное)')
    plt.plot(ema.index, ema, label=f'Экспоненциальное скользящее среднее ({window_size}-дневное)')
    plt.title("Применение метода скользящего среднего и экспоненциального сглаживания")
    plt.xlabel("Месяц")
    plt.ylabel("Значение")
    plt.legend()
    plt.grid(True)
    plt.show()
    name_file = f'amoving_average.png'
    visual.save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)


