a = input("ВВедите слово: ")
b = a.find("#")
if b == -1:
    print("Ошибка")
else:
    print(a[:b:])