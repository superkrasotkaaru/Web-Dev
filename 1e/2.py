# Задача №307. Степень
# Входные данные
# Вводится 2 числа - a (вещественное) и n (целое неотрицательное).

# Выходные данные
# Необходимо вывести  значение an.
def power(a: float, n: int) -> float:
    return a ** n
result = power(*list(map(float, input().split())))
print(result)