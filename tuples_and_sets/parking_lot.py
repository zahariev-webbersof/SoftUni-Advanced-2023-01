def print_func(data):
    if data:
        for car_number in data:
            print(car_number)
    else:
        print('Parking Lot is Empty')

n = int(input())
plate_number_records = [input() for _ in range(n)]
parking_lot_data = set()
COMMAND_IN = 'IN'
COMMAND_OUT = 'OUT'

for record in plate_number_records:
    command, plate_number = record.split(', ')

    if command == COMMAND_IN:
        parking_lot_data.add(plate_number)

    elif command == COMMAND_OUT:
        parking_lot_data.remove(plate_number)

print_func(parking_lot_data)