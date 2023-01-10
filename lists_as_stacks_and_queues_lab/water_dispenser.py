from _collections import deque

def add_names_in_deque():
    people_data = deque()
    while True:
        name = input()

        if name == COMMAND_START:
            break
        people_data.append(name)

    return people_data


COMMAND_END = 'End'
COMMAND_START = 'Start'
COMMAND_REFILL = 'refill '
water_amount = int(input())
people_deque = add_names_in_deque()

while True:
    command = input()

    if command == COMMAND_END:
        print(f'{water_amount} liters left')
        break

    elif command.startswith(COMMAND_REFILL):
        refill_command_data = command.split(' ')
        refill_water_amount = int(refill_command_data[1])
        water_amount += refill_water_amount

    else:
        person = people_deque.popleft()
        current_litres = int(command)

        if current_litres <= water_amount:
            print(f'{person} got water')
            water_amount -= current_litres
        else:
            print(f'{person} must wait')