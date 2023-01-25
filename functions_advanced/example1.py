# # shopping_list = {}
# #
# # def show_list(shopping_list, include_quantities=True):
# #     print()
# #     for item_name, quantity in shopping_list.items():
# #         if include_quantities:
# #             print(f'{quantity} x {item_name}')
# #         else:
# #             print(item_name)
# #
# #
# # def add_items(shopping_list, **things_to_buy):
# #     for item_name, quantity in things_to_buy.items():
# #         shopping_list[item_name] = quantity
# #
# #     return shopping_list
# #
# # shopping_list = add_items(shopping_list, coffee=1, tea=2, cake=1, bread=3)
# # show_list(shopping_list, include_quantities=True    )
#
#
# # languages = ['python', 'ruby', 'c', 'java']
#
# # def select_first_character(word):
# #     return word[0]
# #
# # print(sorted(languages, key=select_first_character))
# # print(sorted(languages, key=lambda word: word[0]))
#
# # numbers = [3, 1, 2, 4, 8, 9, 11]
# #
# # print(sorted(numbers))
# # print(sorted(numbers, key=lambda x: x % 2 == 0))
# # print(sorted(numbers, key=lambda x: x % 2))
#
# # matrix = [[1, 20], [1, 30], [3, 10]]
# #
# # print(sorted(matrix, key=lambda x: max([abs(i) for i in x])))
#
# # my_dict = {'George': 44, 'Peter': 12, 'John': 28}
# # # sorted_dict = sorted(my_dict.items(), key=lambda x: x[0])
# # # print(sorted_dict)
# #
# # # print(sorted(my_dict.items()))
# # print(sorted(my_dict.items(), key=lambda x: x[1]))
# # print(sorted(my_dict.items()))
#
#
# # data = {3: 'D', 2: 'C', 4: 'A', 1: 'B'}
# #
# # print(sorted(data.items()))
# # print(dict(sorted(data.items(), key=lambda item: item[1])))
#
# def has_permission(page):
#     def permission(username):
#         if username.lower() == 'admin':
#             return f'{username.lower()} has right to open {page}'
#         else:
#             return f'{username} does not have right to open {page}'
#     return permission
#
# check_admin_page_permission = has_permission('Admin Page')
# print(check_admin_page_permission('ADMIN'))


# def calculator(operator):
#     def addition(a, b):
#         return a + b
#
#     def subtraction(a, b):
#         return a - b
#
#     def multiplication(a, b):
#         return a * b
#
#     def division(a, b):
#         if a != 0:
#             return a / b
#         else:
#             return 'Value must be greater than zero'
#
#     if operator == '+':
#         return addition
#
#     elif operator == '-':
#         return subtraction
#
#     elif operator == '*':
#         return multiplication
#
#     elif operator == '/':
#         return division
#
#
# calculator_values = calculator('*')
# print(calculator_values(10, 5))


# def func1(a):
#     def func2(b):
#         return a + b
#     return func2
# 
# print(func1(5)(20))


# def countdown(n):
#     print(n)
#
#     if n == 0: # Base case
#         print('end')
#     else:
#         countdown(n - 1)
#
# countdown(5)


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)
#
# print(recur_factorial(3)) # 1 * 2 * 3 = 6
print(recur_factorial(4)) # 1 * 2 * 3 * 4 =


# def function_0():
#     print(0)
#
# def function_1():
#     function_0()
#     print(1)
#
# def function_2():
#     function_1()
#     print(2)
#
# def function_3():
#     function_2()
#     print(3)
#
# function_3()


