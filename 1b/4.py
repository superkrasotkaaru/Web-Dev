# Задача №2959. Знак числа
# sign(x) = 1,   если x > 0,
# sign(x) = -1, если x < 0,
# sign(x) = 0,   если x = 0.

# Для данного числа x выведите значение sign(x).
# Входные данные
# Вводится число x.

# Выходные данные
# Выведите ответ на задачу.

n = int(input())
print(1 if n > 0 else -1 if n < 0 else 0)