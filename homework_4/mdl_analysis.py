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
def analysis_feature(dataset, column):
  try:  
    # Распределение по классу
    target_counts = dataset.groupby(column).size().reset_index(name='count')
    target_counts_df = pd.DataFrame(target_counts, columns=[column, 'count'])
    print(f"\nРаспределение по {column}:")
    print(target_counts_df.T)  
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



