#выводим сколько осталось до дня Х
#
#ввод: 03.09.2023 12.00
#вывод: До часа "Икс" 28 дней и 21 час и 38 минут 
#


import datetime


def choose_plural(num, list_end):
    result = ''
    if num % 100 in range(5, 21):
        result = str(num) + ' ' + list_end[2]
    elif num == 0:
        result = ''
    elif num % 10 in range(2, 5):
        result = str(num) + ' ' + list_end[1]
    elif num % 10 in range(5, 10):
        result = str(num) + ' ' + list_end[2]
    elif num % 10 == 0:
        result = str(num) + ' ' + list_end[2]
    else:
        result = str(num) + ' ' + list_end[0]
    return result


datetime_str = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ : ')

try:

    date_x = datetime.datetime.strptime(datetime_str, '%d.%m.%Y %H:%M')

    date_now = datetime.datetime.now().replace(second=0, microsecond=0)


    if date_x <= date_now:
        print('Ошибка')
    else:
        delta_date = date_x - date_now
        # print(delta_date)

        delta_days = delta_date.days
        delta_hours = delta_date.seconds // 3600
        delta_minutes = (delta_date.seconds % 3600) // 60

        result_st = 'До часа "Икс" '
        choose_st = choose_plural(delta_days, ('день', 'дня', 'дней')).strip()
        if choose_st != '':
            result_st += choose_st + ' '
        if delta_hours > 0 :
            choose_st = choose_plural(delta_hours, ('час', 'часа', 'часов')).strip()
            if delta_days > 0:
                result_st += 'и '
            result_st += choose_st + ' '
        if delta_minutes > 0:
            choose_st = choose_plural(delta_minutes, ('минута', 'минуты', 'минут')).strip()
            if delta_hours > 0 or delta_days > 0:
                result_st += 'и '
            result_st += choose_st + ' '


        print(result_st)

except (ValueError, IndexError):
    print('Ошибка ')




