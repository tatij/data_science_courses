# Файл обучения и предсказания моделей (mdl_classifier.py)
import numpy as np
import seaborn as sns
import sys
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import lightgbm as lgb
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score
import matplotlib.pyplot as plt
import time
sys.path.append('/content/sample_data')
import mdl_visualization as visual

# Визуализация роста цен по признакам
def classifier_data(dataset):
  try:
    dataset.scaler = StandardScaler()
    # Разделение на признаки и целевую переменную
    X = dataset.drop('target', axis=1)  # Все столбцы, кроме target
    y = dataset['target']  # Только столбец target

    # Разделим данные на обучающий и тестовый наборы
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Регрессоры
    classifiers = {
        "Gradient Boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42),
        "ExtraTreesClassifier": ExtraTreesClassifier(n_estimators=100, max_features='sqrt', random_state=42),
        "Quadratic Discriminant Analysis": QuadraticDiscriminantAnalysis(),
        "Light Gradient Boosting Machine": lgb.LGBMClassifier(num_leaves=31, learning_rate=0.05, n_estimators=100, random_state=42),
        "SVC": SVC(kernel='poly', random_state=42)
    }
    results = {}
    for name, model in classifiers.items():
        # Время начала обучения
        time_start = time.time()

        # Создание и обучение классификатора
        clf = model
        clf.fit(X_train, y_train)

        # Время обучения
        times = time.time() - time_start

        # Предсказание на тестовой выборке
        y_pred = clf.predict(X_test)

        # Вычисление метрик
        accuracy = accuracy_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        recall = recall_score(y_test, y_pred, average='weighted')
        precision = precision_score(y_test, y_pred, average='weighted', zero_division=np.nan)

        results[name] = {
            "Accuracy": round(accuracy, 3),
            "Recall": round(recall, 3),
            "Precision": round(precision, 3),
            "Time(s)": round(times, 2)
        }    
        target_names = dataset['target'].unique() 
        visual.visual_matrix(y_test, y_pred, name, target_names)        
    return results
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)



