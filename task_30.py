#вычисление факториала числа через функцию
#

def factorial(n):
    x = 1
    for i in range(1,n + 1):
        x *= i
    return x


print(factorial(int(input('Введите число: '))))
