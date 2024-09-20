def find_password(nom):
    passwords = {}
    numbers = list(range(1, 21))
    for first in numbers:
        for second in numbers[first:]:
            sum_pair = first + second
            if nom % sum_pair == 0:
                pair = f'{first}{second}'
                if pair not in passwords:
                    passwords[pair] = 1
    return ''.join(sorted(passwords.keys()))

def main():
    nom = int(input('Введите число: '))
    if 3 <= nom <= 20:
        password = find_password(nom)
        print(f'Пароль для числа {nom}: {password}')
    else:
        print('Число должно быть в диапазоне от 3 до 20 включительно.')

if __name__ == "__main__":
    main()