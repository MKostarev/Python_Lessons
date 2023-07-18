#генератор пароля

#ввод: 8 (указываем длину пароля)
#вывод: aMw#6a^j

import random
symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+'
len_ = int(input("Введите длину пароля: "))
b = []
for i in range(len_):
    b.append(random.choice(symbols))
c = "".join(b)
print(c)