def create_matrix(rows: int, columns: int):
    matrix = []
    for _ in range(rows):
        matrix.append([0] * columns)

    return matrix


def player_choice(player):
    choice = int(input(f'Player {player}, please choose a column:\n'))

    return choice - 1


def implement_player_data_to_main_logic(playground, player_index, player):
    start_row_index = 0

    while start_row_index < len(playground) and playground[start_row_index][player_index] == 0:
        start_row_index += 1

    playground[start_row_index - 1][player_index] = player

    return start_row_index - 1, player_index


def is_win_condition(player, player_row, player_column, playground, win_counter):

    def convert_player_position_in_direction(playground, initial_row, initial_column, row_change, column_change):
        row, column = initial_row, initial_column
        row_change *= -1
        column_change *= -1

        while 0 <= row < len(playground) and 0 <= column < len(playground[0]):
            if playground[row][column] != player:
                break
            column += column_change
            row += row_change

        if row == initial_row and column == initial_column:
            return row, column

        return row - row_change, column - column_change

    def is_win_condition_in_direction(playground, initial_row, initial_column, direction, win_counter):
        row_change, column_change = direction
        row, column = convert_player_position_in_direction(playground, initial_row, initial_column, row_change, column_change)
        rows_border = min(len(playground), row + win_counter * row_change)
        columns_border = min(len(playground[0]), column + win_counter * column_change)
        row_included_condition = rows_border == row

        counter = 0

        while (row != rows_border or row_included_condition) and (column != columns_border or (columns_border == column)) \
                and player == playground[row][column]:
            counter += 1
            row += row_change
            column += column_change

        return counter == win_counter

    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    for direction in directions:
        if is_win_condition_in_direction(playground, player_row, player_column, direction, win_counter):
            return True
    else:
        return False

def game_play_function(playground, win_counter):
    current_player, second_player = 1, 2

    while True:
        current_player_choice = player_choice(current_player)
        row_index, column_index = implement_player_data_to_main_logic(playground, current_player_choice, current_player)
        print_function(playground)

        if is_win_condition(current_player, row_index, column_index, playground, win_counter):
            print(f'The winner is player {current_player}')
            break

        current_player, second_player = second_player, current_player


def print_function(playground):
    for row in playground:
        print(row)


try:
    rows = int(input('Enter the number of rows: '))
    columns = int(input('Enter the number of columns: '))
    win_counter = int(input('Enter the number of win combination: '))
    playground = create_matrix(rows, columns)
    game_play_function(playground, win_counter)
except ValueError:
    print('Invalid values, try again!')
