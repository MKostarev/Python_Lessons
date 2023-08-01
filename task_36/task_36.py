import csv

with open('task_36.csv') as f:
    rows = csv.reader(f)
    for row in rows:
        print(row)


#import csv
#
#with open('task_36.csv', 'w') as f:
#    writer = csv.writer(f)
#    rows = [
#        ['Борис', 'Минск, Беларусь', 'ул. Ракеты "Булава" 2/10'],
#        ['Виталий', 'Минск', 'сквер "Мотовело"'],
#    ]
#    writer.writerows(rows)