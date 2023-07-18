#выводим количество повторяющихся слов в словаре
#
#ввод: Хвалился, хвалился, да под гору и свалился
#вывод: {'хвалился': 2}

string = "Хвалился, хвалился, да под гору и свалился"
string = string.lower()
string = string.strip()
string = " ".join(string.split())
string = string.replace(",","")
string = string.replace(".","")
b = string.split(" ")
counter = {}
len_ = len(b)
for i in b:
    counter[i] = counter.get(i, 0) + 1
doubles = {element: count for element, count in counter.items() if count > 1}

print(doubles)