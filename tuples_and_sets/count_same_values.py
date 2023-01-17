values = tuple(map(float, input().split(' ')))
values_counter = {}

for value in values:
    if value not in values_counter:
        values_counter[value] = 0
    values_counter[value] += 1

for k, v in values_counter.items():
    print(f'{k} - {v} times')