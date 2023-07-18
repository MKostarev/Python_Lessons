#отделяем слов с цифрами
#
#ввод: !один *два три3,   #четыре, пять5 шесть6
#вывод: word  !один *два #четыре
#       number  три3 пять5 шесть6

string = "!один *два три3,   #четыре, пять5 шесть6"
string = " ".join(string.split())
string = string.replace(",","")
string = string.replace(".","")
b = string.split(" ")
word = []
number = []

for i in b:
    if i.isalnum() == True:
        number.append(i)
    else:
        word.append(i)
word = " ".join(word)
number = " ".join(number)
print("word ", word)
print("number ", number)