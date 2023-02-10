def main_game_logic():
    def get_player_position(matrix, player):
        for row_index, row_data in enumerate(matrix):
            if player in row_data:
                return row_index, row_data.index(player)

    rows, columns = 8, 8
    current_player, second_player = 'w', 'b'
    matrix = [input().split(' ') for _ in range(rows)]
    current_player_position = get_player_position(matrix, current_player)
    second_player_position = get_player_position(matrix, second_player)
    current_change, second_change = -1, +1
    capture_condition, queen_condition = False, False

    while not queen_condition and not capture_condition:
        current_player_row, current_player_column = current_player_position
        second_player_row, second_player_column = second_player_position

        current_player_row += current_change
        current_player_position = (current_player_row, current_player_column)

        if current_player_row == second_player_row and abs(current_player_column - second_player_column) == 1:
            capture_condition = True
            current_player_position = (current_player_row, second_player_column)
        elif current_player_row in [0, rows - 1]:
            queen_condition = True
        else:
            current_player_position, second_player_position = second_player_position, current_player_position
            current_change, second_change = second_change, current_change
            current_player, second_player = second_player, current_player

    return current_player_position, current_player, capture_condition


def print_function(position_data, player_win, capture_condition):
    row, column = position_data
    row_names = [8, 7, 6, 5, 4, 3, 2, 1]
    column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    position_name = f'{column_names[column]}{row_names[row]}'

    if capture_condition:
        return f'Game over! {player_win} win, capture on {position_name}.'
    else:
        return f'Game over! {player_win} pawn is promoted to a queen at {position_name}.'


position_data, current_player, capture_condition = main_game_logic()
player_win = 'White' if current_player == 'w' else 'Black'
print(print_function(position_data, player_win, capture_condition))