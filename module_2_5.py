def get_matrix(n, m, value):

    matrix = []


    for _ in range(n):
        nom = []

        for _ in range(m):
            nom.append(value)
        matrix.append(nom)

    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)