# Файл визуализации датасета (mdl_visualization.py)
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
sys.path.append('/content/sample_data')

def save_plot(fig, filename):
    output_dir = 'sample_data/outputs'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    fig.savefig(file_path)
    print(f"График сохранен: {file_path}")

# Визуализация распределения по признаку
def visual_distribution(dataset, column):
  try:
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(dataset[column], color='skyblue')
    plt.title(f'Распределение по признаку {column}')
    plt.xticks(ha='right', rotation=45, fontsize=8)
    plt.xlabel(column)
    plt.ylabel('Частота')
    plt.show()
    name_file = f'distribution_{column}.png'
    save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Линейная зависимость выживаемости по классу билета
def visual_by_survived(dataset, column):
  try:
    death_counts = dataset[dataset['Survived'] == 0].groupby(column).size()
    death_counts2 = dataset[dataset['Survived'] == 1].groupby(column).size()
    # Построение графика
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.plot(death_counts.index, death_counts.values, marker='o', linestyle='-', color='r', label='Погибшие')
    plt.plot(death_counts2.index, death_counts2.values, marker='o', linestyle='-', color='b', label='Выжившие')
    plt.title(f'Выживаемость по {column}')
    plt.xlabel(column)
    plt.ylabel('Количество погибших')
    plt.xticks(ha='right', fontsize=8)  # Установка меток по оси X
    plt.legend(loc=9)
    plt.grid()
    name_file = f'survived_by_{column}.png'
    save_plot(fig, name_file)
    plt.show()
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Диаграмма рассеяния
def visual_scatter(dataset):
  try:
    price_ticket = []
    for ticket in dataset['Fare']:
      price_ticket.append(float(ticket))
    minY = round(min(price_ticket))
    maxY = round(max(price_ticket))
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.scatter(dataset['Age'], price_ticket)
    plt.title("Диаграмма рассеяния")
    plt.xlabel("Возраст")
    plt.ylabel("Стоимость билета")
    plt.xticks(round(dataset['Age']))
    plt.subplots_adjust(right=4, top=2)
    name_file = f'scatter.png'
    save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

def visual_predictions_scatterplot(y_test, y_pred, name, results):
  try:
    dataset_regressors = pd.DataFrame(results).T
    print(f"Метрики модели: {name}")
    print(dataset_regressors)

    # Для визуализации берем срез значений
    start_index = 5250
    end_index = 5500

    # Визуализация предсказанных и фактических значений
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=y_test[start_index:end_index], y=y_pred[start_index:end_index], color='purple', alpha=0.6)
    plt.plot([y_test[start_index:end_index].min(), y_test[start_index:end_index].max()], [y_test[start_index:end_index].min(), y_test[start_index:end_index].max()], 'r--')
    plt.xlabel('Фактические значения')
    plt.ylabel('Предсказанные значения')
    plt.title(f'Фактические vs Предсказанные значения для цены')
    plt.show()
    name_file = f'predictions_scatterplot_{name}.png'
    save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Визуализация по предсказаниям
def visual_metrics(metrics):
  try:
    dataset_regressors = pd.DataFrame(metrics).T
    print("Сравнение моделей по метрикам:")
    print(dataset_regressors)

    # Визуализация по метрикам
    for name, metric in dataset_regressors.items():    
      fig, ax = plt.subplots(figsize=(6, 4))
      plt.barh(metric.keys(), metric, color='skyblue')
      plt.xlabel(name)
      plt.title(f'Сравнение моделей по {name}')
      plt.show()
      name_file = f'metrics_{name}.png'
      save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)



