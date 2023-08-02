#Форматирование datetime с strftime
#
#

import datetime
my_datetime = datetime.datetime.now()
datetime_str = my_datetime .strftime("%d %b")
print(datetime_str)
datetime_str = my_datetime .strftime("%H:%M")
print(datetime_str)