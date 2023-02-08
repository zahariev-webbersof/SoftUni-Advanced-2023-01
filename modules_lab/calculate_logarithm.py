from math import log

def calculate_log(number, base):
    if base == 'natural':
        print(f'{log(number):.2f}')
    else:
        base = int(base)
        print(f'{log(number, base):.2f}')


number = int(input())
base = input()
calculate_log(number, base)