# Задача №68. Количество элементов больших обоих соседей

# Входные данные
# Сначала задано число N
#  — количество элементов в массиве (1?N?100
# ). Далее через пробел записаны N
#  чисел — элементы массива. Массив состоит из целых чисел.

# Выходные данные
# Необходимо вывести количество элементов массива, у которых два соседа и которые при этом строго больше обоих своих соседей.
n = int(input())
a = list(map(int, input().split()))
cnt = sum(1 for i in range(1, n - 1) if a[i] > a[i - 1] and a[i] > a[i + 1])

print(cnt)