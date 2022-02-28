# Создайте функцию, которая принимает в качестве превого позиционного аргумента имя студента
# и любое число оценок в форме *args
# и выводит в консоль его имя и оценки столбиком
# после этого переработайте функцию таким образом что бы она выводила имя студента и его средний балл

def student_average_score(name, *numbers):
    for i in numbers:
        print(name, i)


student_average_score('Dominik', 1, 2, 3, 4, 5, 4)


def student_average_score_up(name, *numbers):
    return (name, sum(numbers)/len(numbers))


print(student_average_score_up('Dominik', 1, 2, 3, 4, 5, 4))
