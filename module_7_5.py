import os
from datetime import datetime

directory = '.'


for root, dirs, files in os.walk(directory):

    for file in files:
        if file == 'main.py':

            filepath = os.path.join(root, file)

            filetime = os.path.getmtime(filepath)
            formatted_time = datetime.fromtimestamp(filetime).strftime('%d.%m.%Y %H:%M')

            filesize = os.path.getsize(filepath)

            parent_dir = os.path.dirname(filepath)

            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
                  f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')