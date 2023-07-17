catalog = {}

for i in range(3):
    catalog[input('Наименование товара: ').strip()] = int(input('количество товара: ').strip())

print(*[f'{x}: {y}' for x, y in catalog.items() ], sep = '\n')