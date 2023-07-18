#поиск слова, показать сколькло раз оно встречается
#
#ввод: хвалился ,Хвалился, да под гору и свалился
#ввод: хвалился
#вывод: хвалился  =  2

string = "хвалился ,Хвалился, да под гору и свалился"
word = "хвалился"
word = word.lower()
string = string.lower()
string = " ".join(string.split())
string = string.replace(",","")
print(string)
string = string.replace(".","")
b = string.split(" ")
counter = {}
len_ = len(b)
repetition = 0
for i in b:
    if i == word:
        repetition += 1

print(word, " = ", repetition)