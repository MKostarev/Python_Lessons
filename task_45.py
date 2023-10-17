# апельсин, яблоко, мандарин,
# яблоко
# func("я")

def search (spisok, bukva, isBegin):
  dlina1 = 0
  dlina2 = len(bukva)

  if not isBegin:
    dlina1 = -len(bukva)

  filter_spisok = []
  for i in spisok:
    if not isBegin:
      dlina2 = len(i)
    if bukva == i[dlina1:dlina2:]:
      filter_spisok += [i]
  return filter_spisok

spisok = ['апельсин', 'яблоко', 'мандарин', 'банан', 'арбуз']
bukva = input('Введите букву: ')

print(search(spisok, bukva, False))

# True = проверяет с первой буквы
# False = проверяет с последней буквы
