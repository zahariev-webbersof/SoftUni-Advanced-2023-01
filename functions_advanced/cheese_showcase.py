def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda n: (-len(n[1]), n[0]))

    result = []

    for cheese_name, quantity in sorted_data:
        result.append(cheese_name)
        result.extend(sorted(quantity, reverse=True))

    return '\n'.join([str(el) for el in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
