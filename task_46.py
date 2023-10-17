#срезы

# привет
# тевирп
print_word = ''
word = input('Введите слово: ')
for i in range(1, len(word)+1): #range( от чего отчет, до чего(не включительно) отчет, шаг )
  print_word += word[-i]
print (print_word)

#----------
#
#print_word = ''
#word = input('Введите слово: ')
#for i in range(len(word)-1, -1, -1): #range( от чего отчет, до чего(не включительно) отчет, шаг )
#  print_word += word[i]
#print (print_word)
#
#----------
#
#word = input('Введите слово: ')
#print(word[::-1])