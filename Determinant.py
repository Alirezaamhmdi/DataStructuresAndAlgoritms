def read_matrix_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
        rows = file_content.strip().split('\n')
        matrix = [list(map(int, row.split())) for row in rows]
        return matrix
    except Exception as e:
        print(f"Error parsing matrix from file: {e}")
        return None

def switch_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]

def gaussian_elimination(matrix):
    n = len(matrix)

    if n != len(matrix[0]):
        return None
    det = 1

    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[pivot_row][i]):
                pivot_row = j

        if pivot_row != i:
            switch_rows(matrix, i, pivot_row)
            det *= -1

        if matrix[i][i] == 0:
            return 0

        det *= matrix[i][i]

        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]

    return det

def row_column(matrix):
    n = len(matrix)

    if n != len(matrix[0]):
        return None

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0

    for i in range(n):
        sub_matrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
        sign = 1 if i % 2 == 0 else -1
        det += sign * matrix[0][i] * row_column(sub_matrix)

    return det

def rezaifar(matrix):
    n = len(matrix)

    if n != len(matrix[0]):
        return None

    if n == 1:
        return matrix[0][0]

    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    A = [row[1:] for row in matrix[1:]]
    B = [row[:-1] for row in matrix[1:]]
    C = [row[1:] for row in matrix[n:]]
    D = [row[:-1] for row in matrix[n:]]
    E_temp = [row[1:] for row in matrix[1:]]
    E = [row[:-1] for row in E_temp[n-1:]]

    det = ((rezaifar(A) * rezaifar(D)) - (rezaifar(B) * rezaifar(C))) / rezaifar(E)
    return det

file_path = '2.txt'
matrix = read_matrix_from_file(file_path)

if matrix is not None:
    det_gaussian = gaussian_elimination(matrix)
    det_row_col = row_column(matrix)
    det_rezaifar = rezaifar(matrix)

    print(f'Gaussian Elimination: {det_gaussian}')
    print(f'Row and Column: {det_row_col}')
    print(f'RezaiFar: {det_rezaifar}')
