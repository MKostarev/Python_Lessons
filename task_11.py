#Перевернуть список

#ввод:Нет Звука приятнее, чем. Боевой   клич Героев"
#вывод: ['Героев', 'клич', 'Боевой', 'чем', 'приятнее', 'Звука', 'Нет']
#       Героев клич Боевой чем приятнее Звука Нет

string = ("Нет Звука приятнее, чем. Боевой   клич Героев")
string = string.strip()
string = " ".join(string.split())
string = string.replace(",","")
string = string.replace(".","")
b = string.split(" ")
len_ = len(b)
a = []

for i in b[len_::-1]:
    a.append(i)

c = " ".join(a)
print(a)
print(c)