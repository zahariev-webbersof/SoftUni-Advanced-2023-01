def triangle_figure(num):
    figure = ''

    for n in range(1, num + 1):
        for i in range(1, n + 1):
            figure += f'{i} '
        figure += '\n'

    for n in range(num, 0, -1):
        for i in range(1, n):
            figure += f'{i} '
        figure += '\n'

    return figure