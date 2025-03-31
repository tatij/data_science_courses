# Файл визуализации датасета (mdl_visualization.py)
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sys.path.append('/content/sample_data')
from sklearn.metrics import classification_report, confusion_matrix

def save_plot(fig, filename):
    output_dir = 'sample_data/outputs'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    fig.savefig(file_path)
    print(f"График сохранен: {file_path}")

# Визуализация распределения по признаку
def visual_by_feature(dataset, column):
  try:
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(dataset[column], kde=True, bins=123, color='blue')
    plt.title(f'Распределение заболеваний по {column}')
    plt.xlabel(column)
    plt.ylabel('Наличие заболевания')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    name_file = f'visual_by_{column}.png'
    save_plot(fig, name_file)
    plt.show()
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Визуализация предсказанных и фактических значений
def visual_matrix(y_test, y_pred, name, target_names):
  try:  
    conf_matrix = confusion_matrix(y_test, y_pred)
    dataset_classifiers = pd.DataFrame(conf_matrix).T
    print(f"Метрики модели: {name}")
    print(dataset_classifiers)

    # Визуализация матрицы ошибок
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
                xticklabels=target_names,
                yticklabels=target_names)
    plt.xlabel('Предсказанные классы')
    plt.ylabel('Истинные классы')
    plt.title('Матрица ошибок')
    name_file = f'matrix_{name}.png'
    save_plot(fig, name_file)
    plt.show()
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Визуализация по предсказаниям
def visual_metrics(metrics):
  try:
    dataset_classifiers = pd.DataFrame(metrics).T
    print("Сравнение моделей по метрикам:")
    print(dataset_classifiers)

    # Визуализация по метрикам
    for name, metric in dataset_classifiers.items():    
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



