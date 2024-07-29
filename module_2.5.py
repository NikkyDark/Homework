def get_matrix(n, m, value):
    line = [value] * m
    matrix = [line] * n
    return matrix


print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))


