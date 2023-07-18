#бесконечный список дел с перетасовкой при выводе
#
#ввод: первый, второй, третий, четвёртый
#вывод: второй, первый, четвёртый, третий

import random
a = str(input())
i = 0
tasks = []
while a != "":
    tasks.append(a)
    a = str(input())
random.shuffle(tasks)
for i in tasks:
    print(i)
