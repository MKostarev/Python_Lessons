#подсчёт одинаковых слов в каталоге
#ввод: один два два три
#
#вывод: три : 1
#       один : 1
#       два : 2



catalog = {}
slovo = input().lower().replace(',', ' ').replace('.',  ' ').split()
a = set(slovo)
for i in a:
    catalog[i] = slovo.count(i)
for k in catalog:
    print(k,':',catalog[k])