#Обработка исключения конструкция try...except
#
#ввод: 1 в
#вывод: Вы ввели не число


a = input("Введите число")
b = input("Введите число")
try:
    c = int(a)+int(b)
    print(c)
except ValueError:
    print('Вы ввели не число')


