# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - если оно составное.

def is_prime(number) -> bool:
    a = 2
    while number % a != 0:
        a+=1
    return a == number

print(is_prime(9))