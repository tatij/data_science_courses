# Файл визуализации датасета (mdl_visualization.py)
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
sys.path.append('/content/sample_data')

def save_plot(fig, filename):
    output_dir = 'sample_data/outputs'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    fig.savefig(file_path)
    print(f"График сохранен: {file_path}")

# Визуализация торгов
def visual_trading(dataset, column, column2):
  try:
    fig, ax = plt.subplots(figsize=(8, 6))    
    plt.plot(dataset['Date'], dataset[column2], color='red', label=column2)
    plt.plot(dataset['Date'], dataset[column], color='blue', label=column)
    plt.title(f'График торгов {column2} Ethereum')
    plt.legend(loc=9)
    plt.xlabel('Дата')
    plt.ylabel('Стоимость')
    plt.grid()
    plt.show()
    name_file = f'trading_{column2}.png'
    save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Визуализация временного ряда
def visual_series_time(dataset, label):
  try:
    # Визуализируем временной ряд
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(dataset, label='Стоимость открытия торгов')
    plt.title(f"Временной ряд {label}")
    plt.xlabel("Месяц")
    plt.ylabel("Значение")
    plt.grid(True)
    plt.show()
    name_file = f'series_time_{label}.png'
    save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Визуализация автокорреляции и частичной автокорреляции
def visual_autocorrelation(dataset, label):
  try:
    fig, ax = plt.subplots(figsize=(8, 4))
    plot_acf(dataset, ax=ax, lags=40)
    plt.title(f'Автокорреляция {label}')
    plt.show()
    name_file = f'autocorrelation_{label}.png'
    save_plot(fig, name_file)

    fig, ax = plt.subplots(figsize=(8, 4))
    plot_pacf(dataset, ax=ax, lags=40)
    plt.title(f'Автокорреляция (частичная) {label}')
    plt.show()
    name_file = f'autocorrelation_part_{label}.png'
    save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

# Визуализация предсказаний
def visual_prediction(dataset, model, name):
  try:
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(dataset, label='Исходные данные')
    plt.plot(model, label=f'Прогноз {name}')
    plt.title(f'Прогнозирование {name}')
    plt.xlabel('Дата')
    plt.ylabel('Значение')
    plt.legend()
    plt.show()
    name_file = f'prediction_{name}.png'
    save_plot(fig, name_file)
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)

