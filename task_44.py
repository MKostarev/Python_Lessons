#определяем полиндом
number = input('Введите число: ')
isPolydrom = True

start = 0
end = len(number) - 1

while start < end:
  if number[start] != number[end]:
    isPolydrom = False
    break
  start += 1
  end -= 1

if isPolydrom:
  print ('Полиндром')
else:
  print('Не полиндром')

#второй способ определения полиндрома
#number = input('Введите число: ')
#isPolydrom = True

#for i in range(len(number)):
#  if number[i] != number[len(number)-1 - i]:
#    isPolydrom = False
#    break

#if isPolydrom:
#  print ('Полиндром')
#else:
#  print('Не полиндром')

#третий способ определения полиндрома
#number = "543451"
#if number == number[::-1]:
#  print("полиндром")
#else:
#  print("не полиндром")