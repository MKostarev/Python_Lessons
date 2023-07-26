#суммируем всех элементов в строке
#
#ввод: 5, 10, 25, 50, 1, 2, 1
#вывод: 94
#
# Исходная строка с монетками, разделенными запятыми
coin_string = "5, 10, 25, 50, 1, 2, 1"

# Заменяем запятые на пробелы
coins_with_spaces = coin_string.replace(',', ' ')

# Теперь каждая монетка отделена пробелом, и мы можем разделить их и посчитать общую сумму
coin_list = coins_with_spaces.split()
total_amount = sum(int(coin) for coin in coin_list)

print(f"Анна накопила {total_amount} копеек!")