# Задача №113. Список квадратов
# Входные данные
# Задано единственное целое число N

# Выходные данные
# Необходимо вывести  все точные квадраты натуральных чисел, не превосходящие данного числа N.
n, i = int(input()), 1
while i * i <= n:
    print(i ** 2)
    i += 1