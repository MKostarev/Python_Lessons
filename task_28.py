#список продуктов с методом items()
#
#вводим: хлеб 1, нож 3, лист 1
#вывод: хлеб: 2
#       нож: 3
#       лист: 1

catalog = {}

for _ in range(3):
    name = input('Введите наименование: ')
    quant = int(input('Введите количество: '))
    catalog[name] = catalog.get(name, 0) + quant

for key, value in catalog.items():
    print(f'{key}: {value}')