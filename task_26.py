#cортировка одинаковых слов по алфавиту
#
#вводим: один два три два
#вывод: два : 2
#       один : 1
#       три : 1

name = [i for i in input().lower().replace(',', ' ').replace('.',  ' ').split()]
result = {}
for i in name:
    result[i] = result.get(i, 0) + 1

for key, value in sorted(result.items()):
    print(key, ':', value)