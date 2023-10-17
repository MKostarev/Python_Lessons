#калькулятор на функциях

print('Для выхода наберите exit')
#d=3
#print (type(d))
#opiration = ''

#while opiration != 'exit':
#    number1 = input ('Введите первое число: ')
 #   number2 =  input ('Введите второе чило: ')
  #  opiration = input ('Введите операцию : sum, min, umn, del: ' )

 #   if opiration == 'sum':
 #       print(number1 + number2)
 #       opiration = input('Хотите рродолжить? y/n ' )


# проверка на ввод данных
# +проверка на выбор аргумента вычитания
# +выбор функции
# программа не закрывается пока не напишешь exit

def sum_def (number1, number2):
  result = number1 + number2
  return result

def min_def (number1, number2):
  result = number1 - number2
  return result

def del_def (number1, number2):
  result = number1 / number2
  return result

def umn_def (number1, number2):
  result = number1 * number2
  return result

def vvod_def():
  try:
    number1 = input ('Введите первое число: ')
    if number1.isdigit():
      number1 = int(number1)
    else:
      print("Ошибка!")
      return
    argument = input('Введите аргумент (+, -, /, *): ')
    number2 =  int(input ('Введите второе чило: '))
    return (number1, number2, argument)
  except ValueError:
    print("Вы ввели неправильное значение")
    return

def choice_func(a, b, c):
  result = None
  if c == '+':
    result = sum_def(a, b)
  elif c == '-':
    result = min_def(a, b)
  elif c == '/':
    result = del_def(a, b)
  elif c == '*':
    result = umn_def(a, b)
  else:
    result = ('Такого аргумента нет')
  print(f"Результат: {result}")


while exit != 'n':
  numbers = vvod_def()
  if numbers:
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]

    choice_func(a, b, c)
  exit = input('Хотите продолжить? n/y ')