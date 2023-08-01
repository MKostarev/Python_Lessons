import csv

catalog = {}

#  чтение из файла
with open('task_37.csv') as f:
    rows = csv.reader(f)

for line in rows:
    if len(line) > 1:
        catalog[line[0]] = int(line[1])

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

# print(catalog)
catalog = dict(sorted(catalog.items()))
# print(catalog)

with open('task_37.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(catalog.items())

print('\nВ файл записано следующее:')
print(''.join([cat_key + ':' + str(cat_val) + ';\t' for cat_key, cat_val in catalog.items()]))

#import csv
#
#with open('task_37.csv', 'w') as f:
#    writer = csv.writer(f)
#    rows = [
#        ['Борис', 'Минск, Беларусь', 'ул. Ракеты "Булава" 2/10'],
#        ['Виталий', 'Минск', 'сквер "Мотовело"'],
#    ]
#    writer.writerows(rows)