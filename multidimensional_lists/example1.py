# matrix = []
#
# for row in range(3):
#     matrix.append([])
#     for col in range(3):
#         matrix[row].append(col + (row * 3))
#
# # comprehension
# matrix_comprehension = [[col + (row * 3) for col in range(3)] for row in range(3)]
#
# # lambda + comprehension
# make_matrix = lambda x, y, fill: [[fill for _ in range(y)] for _ in range(x)] # m[x][y]
#
#
#
#
#
# print(matrix)
# print(matrix_comprehension)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# new_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
#
# print(new_matrix)

matrix_3d = [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ],
    [
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
]

print(matrix_3d[0])
print(matrix_3d[0][0])
print(matrix_3d[0][0][0])