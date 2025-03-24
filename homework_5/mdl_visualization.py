# Файл визуализации датасета (mdl_visualization.py)
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sys.path.append('/content/sample_data')
import mdl_preprocessing as preproc

def save_plot(fig, filename):
    output_dir = 'sample_data/outputs_recommend'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    fig.savefig(file_path)
    print(f"График сохранен: {file_path}")

# Визуализация выбросов
def visual_outliers_data(dataset, column):
  try:
    # Ящик с усами
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.boxplot(data=dataset[column])
    plt.xticks(rotation=90)
    plt.title(f'График для поиска выбросов {column}')
    plt.show()
    name_file = f'outliers_{column}.png'
    save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Визуализация нормальности распределения target
def visual_hist_target(dataset, target):
  try:
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(dataset[target], kde=True, bins=30, color='skyblue')
    plt.title(f'Гистограмма значений {target}')
    plt.xlabel(target)
    plt.ylabel('Частота')
    plt.show()
    name_file = f'distribution_{target}.png'
    save_plot(fig, name_file)
    print("\nОписание целевой переменной:")
    print(dataset[target].describe())
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Визуализация роста цен по признакам
def visual_by_price(dataset, column):
  try:
    # Группировка по column
    grouped_data = dataset.groupby(column)['price'].mean().reset_index()

    # Построение графика
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=column, y='price', data=grouped_data, palette='viridis')
    plt.title(f'Средняя цена по {column}')
    plt.xlabel(column)
    plt.ylabel('Средняя цена')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    name_file = f'{column}_by_price.png'
    save_plot(fig, name_file)
    plt.show()
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Визуализация предсказанных и фактических значений
def visual_predictions(y_test, y_pred, name, results):
  try:
    dataset_regressors = pd.DataFrame(results).T
    print(f"Метрики модели: {name}")
    print(dataset_regressors)

    # Для визуализации берем срез значений
    start_index = 5000
    end_index = 5500

    # Визуализация предсказанных и фактических значений
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.scatter(range(len(y_test[start_index:end_index])), y_test[start_index:end_index], color='blue', label='Фактические значения')
    plt.scatter(range(len(y_test[start_index:end_index])), y_pred[start_index:end_index], color='red', label='Предсказанные значения')
    plt.xlabel('Наблюдение')
    plt.ylabel('Значение')
    plt.title(f'Фактические и предсказанные значения ({name})')
    plt.legend()
    plt.show()
    name_file = f'predictions_{name}.png'
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



