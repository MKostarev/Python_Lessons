#Определите функцию, которая принимает целочисленный аргумент и возвращает логическое значение trueили falseв зависимости от того, является ли целое число простым.
#
#Согласно Википедии, простое число (или простое число) — это натуральное число, большее, чем 1число, не имеющее положительных делителей, кроме себя 1и себя самого.
#
#Требования
#Вы можете предположить, что вам будет предоставлено целочисленное входное значение.
#Вы не можете предполагать, что целое число будет только положительным. Вам могут быть даны и отрицательные числа ( или 0).
#ПРИМЕЧАНИЕ по производительности : не требуется никаких сложных оптимизаций, но даже самые тривиальные решения могут выйти из строя. Числа могут достигать 2^31 (или около того, в зависимости от языка). Цикл до n, или n/2будет слишком медленным.
#Пример
#is_prime(1)  /* false */
#is_prime(2)  /* true  */
#is_prime(-1) /* false */

import math

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    sqrt_num = int(math.sqrt(number))
    for i in range(5, sqrt_num + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False

    return True