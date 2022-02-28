# Создайте калькулятор с которым можно работать в консоли
# Предложите пользователю ввести по очереди два числа вещественного типа
# Предложите пользователю выбрать действие с ними:
# Доступные операции: +, -, *, /, 0 - exit
# Операции являются функциями.
# Обработать ошибку: “Деление на ноль”

def console_calculator(a,b):
    def plus(a,b):
        print(a+b)
    def minus(a,b):
        print(a-b)
    def mult(a,b):
        print(a*b)
    def div(a,b):
        try:
            a / b
            print(a / b)
        except ZeroDivisionError:
            return ('на ноль делить нельзя')
        print(a/b)
    text = input('шо надо? ')
    if text == '+':
        plus(a,b)
    elif text == '-':
        minus(a,b)
    elif text == '*':
        mult(a,b)
    elif text == '/':
        div(a,b)
    elif text == 0:
        print('вы вышли из калькулятора')

while (console_calculator(int(input('введите первое число')),int(input('введите второе число')))):
    pass



