# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
# Номер месяца вводить с клавиатуры.

def season(month_number) -> str:
    if month_number in range(1,3) or month_number == 12:
        return ('зима')
    elif month_number in range(3,6):
        return ('весна')
    elif month_number in range(6,9):
        return ('лето')
    elif month_number in range(9,12):
        return('осень')
    else:
        return ('неверно введен месяц')
