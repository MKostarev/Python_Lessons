#работа с графикой. рисуем круги

import tkinter
# создаем окно
window = tkinter.Tk()
# создаем холст и размещаем его в окне
canvas = tkinter.Canvas(window)
canvas.pack()

# координаты левого верхнего
# угла прямоугольника, в который должен быть вписан круг
x0 = 50
y0 = 50

# координаты правого нижнего
# угла прямоугольника
x1 = 150
y1 = 150

canvas.create_oval(x0, y0, x1, y1)
canvas.create_oval(0, 0, 200, 200, outline="red")
canvas.create_oval(50, 50, 170, 170, outline="green")
window.mainloop()