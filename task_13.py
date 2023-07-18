#поиск самого длинного слова. вывод слова и его длины
#
#ввод: Нет звука приятнее, чем. боевой клич героев
#приятнее
#8

string = ("Нет звука приятнее, чем. боевой клич героев")
string = string.strip()
string = " ".join(string.split())
string = string.replace(',',"")
string = string.replace('.',"")
b = string.split(' ')
len_ = 0
for i in b:
    if len(i) > len_:
        len_ = len(i)
        big = i
print(big)
print(len(big))
