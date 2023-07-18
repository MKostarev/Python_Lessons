#выводим слова по строчно с номером слова
#
#ввод: !один *два три3,   #четыре, пять5 шесть6
#вывод: 1 !один
#       2 *два
#       3 три3
#       4 #четыре
#       5 пять5
#       6 шесть6
#

string = "!один *два три3,   #четыре, пять5 шесть6"
string = " ".join(string.split())
string = string.replace(",","")
string = string.replace(".","")
b = string.split(" ")
for el in enumerate(b):
    i, e = el
    print(i+1, e)
