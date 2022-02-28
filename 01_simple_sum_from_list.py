# Создайте функцию, которая будет считать сумму чисел в случано сгенерированном массиве длиной 10
# и выводить результат в консоль

from random import randint
lst = [randint(1,10) for i in range(10)]

def summ_lst(list) -> int:
    a = 0
    for i in list:
        a+=i
    return a

print(lst)
print(summ_lst(lst))
