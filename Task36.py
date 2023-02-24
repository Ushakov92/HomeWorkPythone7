# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# Ввод:
# print_operation_table(lambda x, y: x * y)
# Вывод:
#  1   2   3   4   5   6
#  2   4   6   8  10  12
#  3   6   9  12  15  18
#  4   8  12  16  20  24
#  5  10  15  20  25  30
#  6  12  18  24  30  36

import time


def print_operation_table(operation, num_rows=6, num_columns=6):
    # table = ''
    # for i in range(1, num_rows + 1):
    #     for j in range(1, num_columns + 1):
    #         if j == 1:
    #             table += f'{i:<5}'
    #         elif i == 1:
    #             table += f'{j:<5}'
    #         else:
    #             table += f'{abs(operation(i, j)):<5}'
    #     table += '\n'
    # #     table += ''.join([f'{abs(operation(i, j)):<5}'
    # #                       if j != 1 and i != 1 else f'{i:<5}'
    # #                       if j == 1 else f'{j:<5}'
    # #                       for j in range(1, num_columns + 1)]) + '\n'
    #
    # start = time.time()

    table = '\n'.join(
        map(lambda i: ''.join([f'{operation(i, j):5}'
                               if j != 1 and i != 1 else f'{i:5}'
                               if j == 1 else f'{j:5}'
                               for j in range(1, num_columns + 1)]), range(1, num_rows + 1)))
    print(table)

    # time1 = time.time() - start
    #
    # start = time.time()
    #
    # table = list(
    #     map(lambda i: [operation(i, j)
    #                    if j != 1 and i != 1 else i
    #                    if j == 1 else j
    #                    for j in range(1, num_columns + 1)], range(1, num_rows + 1)))
    # # for i in table:
    # #     for j in i:
    # #         print(f'{j:<5}', end='')
    # #     print()
    # list(map(lambda i: [print(f'{j:5}', end='') for j in i] + [print()], table))
    #
    # time2 = time.time() - start
    #
    # timers = [time1, time2]
    #
    # print(*timers)
    # print(f'№ {timers.index(min(timers)) + 1} быстрее')


rows, columns = [int(x) for x in input('Введите кол-во колонок и столбцов : ').split()[:2]]

print_operation_table(lambda x, y: x * y, rows, columns)
