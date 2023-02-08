sequence_of_numbers = []

def create_sequence(number):
    sequence_of_numbers.clear()
    sequence_of_numbers.append(0)
    sequence_of_numbers.append(1)

    for _ in range(number - 2):
        sequence_of_numbers.append(
            sequence_of_numbers[-1] + sequence_of_numbers[-2]
        )

    return ' '.join(map(str, sequence_of_numbers))


def locate_number(element):
    if element in sequence_of_numbers:
        element_index = sequence_of_numbers.index(element)
        return f'The number - {element} is at index {element_index}'
    else:
        return f'The number {element} is not in the sequence'
