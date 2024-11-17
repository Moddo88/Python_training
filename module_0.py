# 1st program
print(9**0.5 * 5)

# 2nd program
print((9.99 > 9.98) and (1000 != 1000.1))

# 3rd program
print(2 * 2 + 2)        # Без приоритета
print(2 * (2 + 2))      # С приоритетом для сложения
print((2 * 2 + 2) == (2 * (2 + 2)))

# 4th program
number = float('123.456')
shifted_number = number * 10
first_digit_after_point = int(shifted_number) % 10
print(first_digit_after_point)