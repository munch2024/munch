#2.2
def matrix_multiply(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            product = 0
            for k in range(len(matrix_b)):
                product += matrix_a[i][k] * matrix_b[k][j]
            row.append(product)
        result.append(row)
    return result
