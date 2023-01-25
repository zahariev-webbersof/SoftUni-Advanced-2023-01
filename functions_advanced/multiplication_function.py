# def multiply(*args):
#     product = 1
#     for num in args:
#         product *= num
#
#     return product
#
# print(multiply(1, 4, 5))
# print(multiply(4, 5, 6, 1, 3))
# print(multiply(2, 0, 1000, 5000))
from  functools import reduce

def multiply(*args):
    return reduce(lambda x, y: x * y, args)

print(multiply(0, 0, 0))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
