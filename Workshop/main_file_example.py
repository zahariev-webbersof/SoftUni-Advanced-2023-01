def create_matrix(rows: int, columns: int):
    matrix = []
    for _ in range(rows):
        matrix.append([0] * columns)

    return matrix

# В тази функция ще обработваме входа от потребителя
def player_choice(player):
    # player please чуус а калъмн
    choice = int(input(f'Player {player}, please choose a column:\n'))
    # Тук може да го направим и с минус едно, защото играча казва 1, пък може би има предвид колона 0-ла
    return choice - 1

# Тук всъщност ще обработваме дейтата спрямо логиката на играта
def implement_player_data_to_main_logic(playground, player_index, player):
    start_row_index = 0

    # това ни е условието на база на което ще
    # въртим до момента в който не срещнем нещо различно от 0-ла
    while start_row_index < len(playground) and playground[start_row_index][player_index] == 0:
        start_row_index += 1

    playground[start_row_index - 1][player_index] = player

    return start_row_index - 1, player_index

# А тук ще проверяваме дали случайно нямаме 4 поредни знака и следователно победа
def check_win_condition(playground, row_index, column_index, win_counter):

    def check_right_win_condition(playground, row_index, column_index, max_column_index):
        right_values = [playground[row_index][i] for i in range(column_index, max_column_index)]
        return right_values

    def check_left_win_condition(playground, row_index, column_index, min_column_index):
        left_values = [playground[row_index][i] for i in range(column_index, min_column_index, -1)]
        return left_values

    def check_up_win_condition(playground, row_index, column_index, min_row_index):
        # min row index защото отиваме нагоре и намаляме
        up_values = [playground[i][column_index] for i in range(row_index, min_row_index, -1)]
        return up_values

    def check_down_win_condition(playground, row_index, column_index, max_row_index):
        down_values = [playground[i][column_index] for i in range(row_index, max_row_index)]
        return down_values

    # Тук започваме да проверяваме диагоналите - 1ви е надолу и наляво
    def check_down_right_win_condition(playground, row_index, column_index, max_row_index, max_column_index):
        index = min(max_row_index - row_index, max_column_index - column_index)
        down_right_values = [playground[row_index + i][column_index + i] for i in range(index)]
        return down_right_values

    def check_down_left_win_condition(playground, row_index, column_index, max_row_index, min_column_index):
        index = min(max_row_index - row_index, abs(min_column_index - column_index))
        down_right_values = [playground[row_index + i][column_index - i] for i in range(index)]
        return down_right_values

    # нагоре и надясно
    def check_up_right_win_condition(playground, row_index, column_index, min_row_index, max_column_index):
        index = min(abs(min_row_index - row_index), max_column_index - column_index)
        # тъй като сега отиваме нагоре ще намаляме реда, а колоните се увеличават
        down_right_values = [playground[row_index - i][column_index + i] for i in range(index)]
        return down_right_values

    def check_up_left_win_condition(playground, row_index, column_index, min_row_index, min_column_index):
        index = min(abs(min_row_index - row_index), abs(min_column_index - column_index))
        # тъй като сега отиваме нагоре ще намаляме реда, а колоните се увеличават
        down_right_values = [playground[row_index - i][column_index - i] for i in range(index)]
        return down_right_values


    # indexes

    # Сетваме си максималният индекс възможен в зависимост от това къде се намираме в реда
    # Съответно което е по-малко ще го вземе
    max_column_index = min(column_index + win_counter, len(playground[column_index]))

    # Тъй като не искаме по-малко от 0-ла, съпоставяме с нея
    min_column_index = max(-1, column_index - win_counter)

    # Ще ползваме най-малкият row index тъй като ще ходим нагоре и ще намалява
    max_row_index = min(row_index + win_counter, len(playground))

    # Ще ползваме най-малкият row index тъй като ще ходим нагоре и ще намалява
    min_row_index = max(row_index - win_counter, -1)

    # left, right, up and down directions
    right_win_condition_values = check_right_win_condition(playground, row_index, column_index, max_column_index)
    left_win_condition_values = check_left_win_condition(playground, row_index, column_index, min_column_index)
    up_win_condition_values = check_up_win_condition(playground, row_index, column_index, min_row_index)
    down_win_condition_values = check_down_win_condition(playground, row_index, column_index, max_row_index)

    # diagonals
    down_right_win_condition_values = check_down_right_win_condition(playground, row_index, column_index, max_row_index
                                                                     , max_column_index)
    down_left_win_condition_values = check_down_left_win_condition(playground, row_index, column_index, max_row_index
                                                                   , min_column_index)
    up_right_win_condition_values = check_up_right_win_condition(playground, row_index, column_index, min_row_index
                                                                 , max_column_index)
    up_left_win_condition_values = check_up_left_win_condition(playground, row_index, column_index, min_row_index
                                                               , min_column_index)

    possible_winner_checker = [
        right_win_condition_values,
        left_win_condition_values,
        down_win_condition_values,
        up_win_condition_values,
        down_right_win_condition_values,
        down_left_win_condition_values,
        up_right_win_condition_values,
        up_left_win_condition_values,
    ]

    # for current_elements in possible_winner_checker:
    #     if len(current_elements) == win_counter and len(set(current_elements)) == 1:
    #         return True
    # return False

    return any(len(current_elements) == win_counter and len(set(current_elements)) == 1 for current_elements in possible_winner_checker)

# Това ще е нещото което ще управлява основната логика, кой играч е наред и т.н.
# Тук в play ще подаваме игралното поле
def game_play_function(playground, win_counter):
    # тук си сетваме двата играча
    current_player, second_player = 1, 2
    # win_counter = 4
    while True:
        # така доста лесно може да сглобим нещата
        current_player_choice = player_choice(current_player)
        row_index, column_index = implement_player_data_to_main_logic(playground, current_player_choice, current_player)
        print_gameplay_data(playground)
        if check_win_condition(playground, row_index, column_index, win_counter):
            print(f'Player {current_player} wins!')
            break

        # това ще го правим за да им разменяме позициите, за да се редуват
        current_player, second_player = second_player, current_player


def print_gameplay_data(playground):
    for row in playground:
        print(row)


try:
    rows = int(input('Enter the number of rows: '))
    columns = int(input('Enter the number of rows: '))
    win_combination = int(input('Enter the number of win combination: '))
    playground = create_matrix(rows, columns)
    game_play_function(playground, win_combination)

except ValueError as err:
    print('Invalid values')
