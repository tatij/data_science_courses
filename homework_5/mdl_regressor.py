# Файл обучения и предсказания моделей (mdl_regressor.py)
import matplotlib.pyplot as plt
import sys
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from lightgbm import LGBMRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import VotingRegressor
import numpy as np
import time
sys.path.append('/content/sample_data')
import mdl_visualization as visual

# Визуализация роста цен по признакам
def regressor_data(dataset):
  try:
    dataset.scaler = StandardScaler()
    # Разделение на признаки и целевую переменную
    X = dataset.drop('price', axis=1)  # Все столбцы, кроме target
    y = dataset['price']  # Только столбец target

    # Разделим данные на обучающий и тестовый наборы
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Регрессоры
    regressor = {      
      "XGBoost": XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42),
      "LGBMRegressor": LGBMRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42),
      "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42),      
      "DecisionTreeRegressor": DecisionTreeRegressor(random_state=42),
      "VotingRegressor": VotingRegressor(estimators=[
        ('gb', GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)),
        ('lgbm', LGBMRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)),
        ('xgb', XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42))        
      ])
    }
    results = {}
    for name, model in regressor.items():
        # Время начала обучения
        time_start = time.time()

        # Создание и обучение классификатора
        model.fit(X_train, y_train)

        # Время обучения
        times = time.time() - time_start

        # Предсказание на тестовой выборке
        y_pred = model.predict(X_test)

        # Вычисление метрик
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        results[name] = {
            "MAE": round(mae, 0),
            "MSE": round(mse, 0),
            "RMSE": round(rmse, 0),
            "R²": round(r2, 4),
            "Time(s)": round(times, 1)
        }
        visual.visual_predictions(y_test, y_pred, name, results)
    return results
  except FileNotFoundError as e:
        print(f"Ошибка при загрузке данных: {e}")
        sys.exit(1)



