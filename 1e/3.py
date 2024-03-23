# Задача №308. Исключающее ИЛИ
# Входные данные
# Вводится 2 числа - x и y (x и y равны 0 или 1, 0 соответствует значению false, 1 соответствует значению true).

# Выходные данные
# Необходимо вывести 0 или 1 - значение функции от x и y.

def xor(x: bool, y: bool) -> bool:
    return (x or y) and not (x and y)

x, y = map(int, input().split())
print(int(xor(bool(x), bool(y))))