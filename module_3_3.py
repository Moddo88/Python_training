def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)

# Функция с параметрами по умолчанию
print("--- Функция с параметрами по умолчанию ---")
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параметров
print("--- Распаковка параметров ---")
values_list = ['Строка', 100, False]
values_dict = {'a': 'Строка', 'b': 123, 'c': 'true'}
print_params(**values_dict)

# Распаковка + отдельные параметры
print("--- Распаковка + отдельные параметры ---")
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)