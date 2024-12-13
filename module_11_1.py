import pandas as pd

# Загрузка данных
df = pd.read_csv('data.csv')

# Статистика данных
print(df.describe())

# Фильтрация
filtered_df = df[df['value'] > 10]
print(filtered_df.head())

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    data = response.json()
    print("Заголовок:", data['title'])
else:
    print("Ошибка запроса:", response.status_code)


import matplotlib.pyplot as plt

# Данные
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Построение графика
plt.plot(x, y, marker='o')

# Настройка графика
plt.title("Пример графика")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

# Сохранение и отображение
plt.savefig("graph.png")
plt.show()


