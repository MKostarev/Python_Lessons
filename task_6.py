#выводим текст справо на лево (ru)

#display text from right to left (en)

string = input()
string = string.upper()
string = string.replace(" ", "")
a = string[::-1]
print(a)