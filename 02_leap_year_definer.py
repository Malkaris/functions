# Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.
# признаки високосного года:
# - если год делится нацело на 4 - возможно он високосный
# - если год делится на 4 но не делится нацело на 100 - он високосный
# - если год делится на 4, делится на 100 - возможно он не високосный
# - если год делится на 4, делится на 100 и делится нацело на 400 - он високосный
# Тесты:
# - високосные: 2000, 1996, 2012, 2016
# - не високосные: 1900, 1997, 1700, 1500

# после 08 задания переработайте функцию таким образом что бы она принимала в себя любое количество
# годов и выводила в консоль соответсвующее число строк вида:
# 2000 - високосный год
# 1900 - не високосный год