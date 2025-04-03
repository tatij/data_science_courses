# Файл визуализации датасета (mdl_visualization.py)
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def save_plot(fig, filename):
    output_dir = 'sample_data/outputs'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    fig.savefig(file_path)
    print(f"График сохранен: {file_path}")

# Визуализация распределения по признакам
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

# Визуализация роста цен по признакам
def visual_lineplot_by_feature(dataset, column):
  try:
    # Построение графика
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(dataset, x = dataset[column], y = dataset["Price ($)"])
    plt.title(f"Линейная зависимость цены от {column}")
    plt.xticks(ha='right', rotation=45, fontsize=8)
    plt.xlabel(column)
    plt.ylabel("Цена")
    plt.show()  
    name_file = f'lineplot_by_{column}.png'
    save_plot(fig, name_file)
    plt.show()
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Диаграмма рассеяния
def visual_scatterplot(dataset):
  try:
    # Диаграмма рассеяния (цена, бренд, расшерение)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='Brand', y='Price ($)', hue='Resolution', style='Resolution', data=dataset, s=100)
    plt.title(f'Диаграмма рассеяния расшерения по цене и бренду')
    plt.xticks(rotation=123, ha='right', fontsize=8)
    plt.xlabel('Бренд')
    plt.ylabel('Цена')
    plt.show() 
    name_file = f'scatterplot.png'
    save_plot(fig, name_file)
    plt.show()
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)




