def check_left_win_condition(playground, row_index, column_index, min_column_index):
    left_values = [playground[row_index][i] for i in range(column_index, min_column_index, -1)]
    return left_values

result = check_left_win_condition(
    playground=[
        [0, 0, 0, 0, 0, 0, 0],
        [1, 2, 2, 2, 1, 1, 1],
    ],
    row_index=1,
    column_index=4,
    min_column_index=0
)

print(result)

