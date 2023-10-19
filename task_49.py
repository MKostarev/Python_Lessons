#тренировка классов

class Fruit():
    def __init__(self, name, time, color, count):
        self.Name = name
        self.Time = time
        self.Color = color
        self.Count = count
        pass

    def Info(self):
        print(
            f'Информация о фрукте: \nИмя: {self.Name}, \nВремя созревания: {self.Time}, \nЦвет: {self.Color}, \nКоличество: {self.Count}')

    def Eat(self, count=1):
        if self.Count >= count:
            self.Count -= count
            print(f'Вкусно покушали. Количество {self.Name} оставлось: {self.Count}')
        else:
            print(f'У вас {self.Name} не хватает!')


oranges = Fruit('Апельсин', 'Месяц', 'Оранжевый', 3)
oranges.Info()
oranges.Eat()

apples = Fruit('Яблоко', 'Два месяца', 'Зелёный', 5)
apples.Info()