#шифр цезаря
alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' # 33 символа
alphabet_upper = alphabet_lower.upper()
word = input('Введите фразу: ')
shift = int(input('Введите свдиг: '))

encrypted_word = ''

for char in word:
  if char.isalpha(): # Проверяет это буква ли
    if char.isupper():
      alphabet = alphabet_upper
    else:
      alphabet = alphabet_lower
    index = alphabet.index(char)
    new_index = (index + shift) % 33
    encrypted_word += alphabet[new_index]
  else:
    encrypted_word += char
print(f'Зашифрованное сообщение:  {encrypted_word}')