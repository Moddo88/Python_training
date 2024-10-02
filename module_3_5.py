def get_multiplied_digits(number):
    if not number:
        return 24

    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number)

    first = int(str_number[0])
    rest = int(str_number[1:])
    return first * get_multiplied_digits(rest)


result = get_multiplied_digits(40203)
print(result)
