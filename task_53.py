# move - (-5)
# take(предмет) - если вес предмета больше силы, то робот не может поднять предмет. В ином случае, выводится сообщение об успешном поднятии.

# ПРЕДМЕТ - отдельный класс, с параметрами: имя, вес.
# предмет кружка
# предмет гиря
# предмет машина

class Robot ():
  def __init__(self, name, power): #конструктор класса, name и power - параметры
    self.Name = name  #создание переменных для класса осуществляется внутри коснтурнктора
    self.Power = power
    self.Road = [0] * 10
    self.Road[6] = 1

  def Hellow(self):      #функция внутри класса называется методом. Метод пишется с заглавной буквы.
    print(f'Привет! Меня зовут {self.Name}.')

  def Move(self, step):
    print(f"Старая позиция: {self.Road}")
    current_pos = self.Road.index(1)
    self.Road = [0] * 10
    new_pos = current_pos + step
    if new_pos < 0:
      new_pos = 0
      print(f"Робот уперелся в стену. Передвинулся с позиции {current_pos} на позицию {new_pos}")
    elif new_pos > (len(self.Road) - 1):
      new_pos = (len(self.Road) - 1)
      print(f"Робот уперелся в стену. Передвинулся с позиции {current_pos} на позицию {new_pos}")

    self.Road[new_pos] = 1
    print(f"Новая позиция: {self.Road}")
    pass

  def Take():
    pass

robokop = Robot('Boston Dainemiks', 15) #для вызова функции, сначала нужно создать экземпляр класса
robokop.Hellow() #вызываем функцию класса
robokop.Move(10)