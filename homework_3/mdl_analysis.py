# Файл анализа датасета (mdl_analysis.py)
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sys.path.append('/content/sample_data')
import mdl_visualization as visual
from sklearn.preprocessing import LabelEncoder

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

# Кодирование категориальных признаков
def encoder_feature(dataset):
  try:
    label_encoder = LabelEncoder()
    dataset['Sex_int'] = label_encoder.fit_transform(dataset['Sex'])          
    return dataset
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



