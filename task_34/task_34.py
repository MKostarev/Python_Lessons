#работа с файлами. выводи то что в файле
#
#


f = open('C:/Работа/Python/Letpy_training/Python_tasks/task_34/task_34.txt')
#f.write('Важная информация\n')
#f.write('Вторая по важности информация')
#f.close()
content = f.read()
print(content)