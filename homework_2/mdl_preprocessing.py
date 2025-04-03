# Файл предобработки датасета (mdl_preprocessing.py)
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Кодирование категориальных признаков
def encoder_feature(dataset):
  try:
    dataset_feature = {
        'Brand_int': dataset['Brand'],
        'Processor_int':  dataset['Processor'],
        'Storage_int':  dataset['Storage'],
        'GPU_int':  dataset['GPU'],
        'Resolution_int':  dataset['Resolution'],
        'Operating System_int':  dataset['Operating System']
        }
    dataset_feature = pd.DataFrame(dataset_feature)
    label_encoder = LabelEncoder()
    for name, value in dataset_feature.items():
      dataset[name] = label_encoder.fit_transform(value)         
    return dataset
  except FileNotFoundError as e:
    print(f"Ошибка при загрузке данных: {e}")
    sys.exit(1)




