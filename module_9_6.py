def all_variants(text):
    """
    Функция-генератор, которая возвращает подпоследовательности строки text.
    """
    n = len(text)
    for length in range(1, n + 1):  # длина подпоследовательности
        for start in range(n - length + 1):  # начальная позиция
            yield text[start:start + length]

# Пример использования
a = all_variants("abc")
for i in a:
    print(i)
