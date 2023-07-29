#выбор формы существительного
#
#ввод: 15
#вывод: 15 бананов
#
#

def choose_plural(n,m):
    if n % 10 == 1 and n % 100 != 11 :
        return f'{n} {m[0]}'
    elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
        return f'{n} {m[1]}'
    else:
        return f'{n} {m[2]}'

print(choose_plural(int(input('кол-во ')), ('банан', 'банана', 'бананов')))