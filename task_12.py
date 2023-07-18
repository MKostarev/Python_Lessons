#Удаление "." и ",". Выделение красным цветом слов с заглавных букв
#
#ввод: Нет Звука приятнее, чем. Боевой клич Героев
#вывод: Нет Звука приятнее чем Боевой клич Героев

from colorama import Fore
string = ("Нет Звука приятнее, чем. Боевой клич Героев")
string = string.strip()
string = " ".join(string.split())
string = string.replace(',',"")
string = string.replace('.',"")
b = string.split(' ')
text = ""
i = 0
for i in b:
    if i.istitle():
        text = text + ' ' + Fore.RED + i
    else:
        text = text + ' ' + Fore.RESET + i
print(text)