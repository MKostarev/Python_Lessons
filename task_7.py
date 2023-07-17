#провекра введённого значение на >= 8.
#если длина больше 8 то выводим посление 4 знака, а остальные знаки меняем на *
#резкльтат работы:
#вводим: 12345678
#результат: Всё норм
#           ****5678
#иначе результат: ошибка

pass_word = input()
length_pass_word = len(pass_word)
if pass_word.isdigit() and length_pass_word >= 8:
    print("Всё норм")
    length_pass_word = int(length_pass_word)
    star = "*" * (length_pass_word - 4)
    pass_word = star + pass_word[-4::]
    print(pass_word)
else:
    print("Ошибка")