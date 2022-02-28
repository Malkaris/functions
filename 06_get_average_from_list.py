# Создайте функцию вычисляющую среднее арифметическое элементов массива.
# Массив должен состоять из случайных чисел, длинной 10 элементов.

from random import randint

lst = [randint(1, 1000) for i in range(10)]


def get_average_from_list(list) -> float:
    res = sum(lst) / len(lst)
    return res


print(lst)
print(get_average_from_list(lst))
