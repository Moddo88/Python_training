class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError("шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # начальная позиция итерации

    def __iter__(self):
        self.pointer = self.start  # сброс pointer на старт
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration  # завершение итерации
        current = self.pointer
        self.pointer += self.step  # перемещение pointer на шаг
        return current

# Примеры использования
try:
    iter1 = Iterator(100, 200, 0)  # Шаг равен 0 — выброс исключения
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print("Шаг указан неверно")

iter2 = Iterator(-5, 1)  # Шаг по умолчанию равен 1
iter3 = Iterator(6, 15, 2)  # Шаг равен 2
iter4 = Iterator(5, 1, -1)  # Шаг равен -1
iter5 = Iterator(10, 1)  # Шаг по умолчанию 1, но условия не позволяют итерацию

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
