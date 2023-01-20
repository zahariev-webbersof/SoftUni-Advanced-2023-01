matrix = [[int(el) for el in input().split(', ')] for _ in range(int(input()))]
result = [num for row in matrix for num in row]
print(result)

# number_of_rows = int(input())
# matrix = []
# for row in range(number_of_rows):
#     row_data = list(map(int, input().split(', ')))
#     matrix.append(row_data)
#
# new_matrix = []
#
# for row in matrix:
#     for num in row:
#         new_matrix.append(num)
#
# print(new_matrix)