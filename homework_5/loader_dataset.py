# Файл загрузки датасета (loader_dataset.py)
import pandas as pd
import sys
import csv

def load_csv_file(path):
  try:
    csv_file = pd.read_csv(path, index_col=False, decimal='.', delimiter=';')
    print("Данные успешно загружены.")
    return csv_file
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)