def read_matrix_func():
    number_of_rows = int(input())
    current_matrix = []

    for row in range(number_of_rows):
        row_data = list(map(int, input().split(' ')))
        current_matrix.append(row_data)

    return current_matrix


matrix = read_matrix_func()


def get_sum_of_primary_diagonal(matrix):
    sum_of_primary_diagonal = [matrix[i][i] for i in range(len(matrix))] # [11, 4, -12]
    return sum(sum_of_primary_diagonal)


def get_sum_of_secondary_diagonal(matrix):
    sum_of_secondary_diagonal = 0
    for i in range(len(matrix) - 1, -1, -1): # i=2, i=1, i=0
        sum_of_secondary_diagonal += matrix[i][(len(matrix) - 1) - i]
    return sum_of_secondary_diagonal


def get_sum_of_left_half(matrix):
    sum_of_elements = 0
    matrix_size = len(matrix)
    for row in range(matrix_size):
        for column in range(row + 1):
            sum_of_elements += matrix[row][column]

    return sum_of_elements


def get_sum_of_right_half(matrix):
    sum_of_elements = 0
    matrix_size = len(matrix)
    for row in range(matrix_size):
        for column in range(row, matrix_size):
            sum_of_elements += matrix[row][column]

    return sum_of_elements

print(get_sum_of_primary_diagonal(matrix))
# print(get_sum_of_secondary_diagonal(matrix))
# print(get_sum_of_left_half(matrix))
# print(get_sum_of_right_half(matrix))