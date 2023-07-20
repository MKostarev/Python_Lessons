#заполняем каталог товаров из 3 позиций
#
#ввод:  Введите наименование товара хлеб
#       Введите количество товара 2
#       Введите наименование товара бумага
#       Введите количество товара 3
#       Введите наименование товара картошка
#       Введите количество товара 4
#
#вывод: хлеб:2
#       бумага:3
#       картошка:4


catalog = {}
count = 0
for i in enumerate(range(1,4)):
    name = input("Введите наименование товара")
    quantity = input("Введите количество товара")
    catalog[name] = quantity
    count += 1
    name_2 = input("Введите наименование товара")
    quantity_2 = input("Введите количество товара")
    catalog[name_2] = quantity_2
    count += 1
    name_3 = input("Введите наименование товара")
    quantity_3 = input("Введите количество товара")
    catalog[name_3] = quantity_3
    count += 1
    break
for k in catalog:
        print(k, catalog[k], sep = ":")


#cловари и оператор in
#
#catalog = {}
#
#for _ in range(3):
#    name = input('Введите наименование: ')
#    quant = int(input('Введите количество: '))
#    catalog[name] = catalog.get(name, 0) + quant
#
#print(catalog)

