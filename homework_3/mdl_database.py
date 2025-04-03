# Файл базы данных (mdl_database.py)
import sqlite3
import sys
import pandas as pd

# Создание и подключение к бд
def create_db(name_db):
  try:
    conn = sqlite3.connect(name_db)
    cursor = conn.cursor()
    print(f"БД {name_db} создана")
    return cursor
  except FileNotFoundError as e:
    print(f"Ошибка при подключение к бд: {e}")
    sys.exit(1)

# Удаление таблицы в бд
def drob_tbl(cursor, table):
  try:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    print(f"Таблица {table} удалена")
  except FileNotFoundError as e:
    print(f"Ошибка при удаление таблицы {table} в бд: {e}")
    sys.exit(1)

# Создание таблицы в бд
def create_tbl(cursor, table, columns):
  try:    
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table} ({columns})')
    print(f"Добавлена таблица {table} в бд")
  except FileNotFoundError as e:
    print(f"Ошибка при создание таблицы {table} в бд: {e}")
    sys.exit(1)

# Добавление данных в таблицу в бд
def load_tbl(name_db, table, dataset):
  try:
    conn = sqlite3.connect(name_db)
    dataset.to_sql(table, con=conn, if_exists='append', index=False)
    print(f"Данные добавлены в таблицу {table} в бд")
  except FileNotFoundError as e:
    print(f"Ошибка при добаление данных в таблицу {table} в бд: {e}")
    sys.exit(1)

# Удаление записи из таблицы в бд
def delete_string(cursor, table, column, value):
  try:    
    cursor.execute(f'DELETE FROM {table} WHERE {column} {value}')
    print(f"Запись в таблице {table} удалена")
  except FileNotFoundError as e:
    print(f"Ошибка при удаление записи таблицы {table}: {e}")
    sys.exit(1)

def select_tbl(cursor, table, outputs, condition):
  try:    
    cursor.execute(f"SELECT {outputs} FROM {table} {condition}")
    dataset = cursor.fetchall()
    print(f"\nЗапрос в таблицу {table} выполнен")
    return dataset    
  except FileNotFoundError as e:
    print(f"Ошибка запроса в таблице {table}: {e}")
    sys.exit(1)

# Закрытие соединения и сохранение изменений
def close_connect(name_db):
  try:    
    conn = sqlite3.connect(name_db)
    conn.commit()
    conn.close()
    print(f"Соединение с бд {name_db} закрыто")
  except FileNotFoundError as e:
    print(f"Ошибка при закрытия соединения с бд {name_db}: {e}")
    sys.exit(1)


