#калькулятор на классе

class Calc():
    def Sum_def(self, number1, number2):
        result = number1 + number2
        return result

    def Min_def(self, number1, number2):
        result = number1 - number2
        return result

    def Del_def(self, number1, number2):
        result = number1 / number2
        return result

    def Umn_def(self, number1, number2):
        result = number1 * number2
        return result

    def Choice_func(self, a, b, c):
        result = None
        if c == '+':
            result = self.Sum_def(a, b)
        elif c == '-':
            result = self.Min_def(a, b)
        elif c == '/':
            result = self.Del_def(a, b)
        elif c == '*':
            result = self.Umn_def(a, b)
        else:
            result = ('Такого аргумента нет')
        print(f"Результат: {result}")
        pass

    def Vvod_def(self):
        try:
            number1 = input('Введите первое число: ')
            if number1.isdigit():
                number1 = int(number1)
            else:
                print("Ошибка!")
                return
            argument = input('Введите аргумент (+, -, /, *): ')
            number2 = int(input('Введите второе чило: '))
            return (number1, number2, argument)
        except ValueError:
            print("Вы ввели неправильное значение")
            return

    def Start(self):
        exit = ''
        while exit != 'n':
            numbers = self.Vvod_def()
            if numbers:
                a = numbers[0]
                b = numbers[1]
                c = numbers[2]

                self.Choice_func(a, b, c)
        exit = input('Хотите продолжить? n/y ')


calc = Calc()
calc.Start()