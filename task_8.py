#выделить числа из строки и отсортировать их
#ввод: WER1hg5jhg3jhg
#результат работы: [1, 3, 5]

string = "WER1hg5jhg3jhg"
word = []
number = []
for i in string:
    if i.isdigit():
        number.append(int(i))
number = sorted(number)
print(number)