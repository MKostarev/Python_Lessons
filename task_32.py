#шифрование Цезаря
#
#ввод: ПРИВЕТ, МИР!
#вывод: ЩЪТЛОЬ, ЦТЪ!


letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890 !'
#          012345678901234567890123456789012345678901234
#                    1         2         3         4
#

def encrypt (text, num):
    result = ''
    for sym in text.strip().upper():
        if sym in letters:
            id_crypt = letters.find(sym) + num
            result += letters[id_crypt % len(letters)]
        else:
            result += sym
    return result


message = "Привет Виктор! Сегодня 22 мая 2023 года! 1 час ночи 32 минуты! Иди спать"
# print(message.upper())
encrypted_message = encrypt(message, 10)
print(encrypted_message)
decrypted_message = encrypt(encrypted_message, -10)
print(decrypted_message)
