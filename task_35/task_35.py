#каталог товаров с сохранением

catalog = {}
#  чтение из файла
with open('task_35.txt', 'r+') as f:
    lines = f.readlines()

for line in lines:
    st_line = line.strip().split(':')
    catalog[st_line[0]] = int(st_line[1])

#  вывод на экран содержимого файла
print('Из файла прочитано следующее:')
print(''.join([cat_key + ':' + str(cat_val) + ';\t' for cat_key, cat_val in catalog.items()]))

for i in range(3):
    user_in1 = input('Товар: ')
    user_in2 = int(input('Количество: '))
    if user_in1 in catalog.keys():
        catalog[user_in1] += user_in2
    else:
        catalog[user_in1] = user_in2

catalog = dict(sorted(catalog.items()))

with open('task_35.txt', 'w') as f:
    f.write(''.join([cat_key + ':' + str(cat_val) + '\n' for cat_key, cat_val in catalog.items()]))

print('\nВ файл записано следующее:')
print(''.join([cat_key + ':' + str(cat_val) + ';\t' for cat_key, cat_val in catalog.items()]))

