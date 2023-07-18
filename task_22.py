#рисуем случайно круги (бесконечно)
import tkinter
import random
import time
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()

colors = ('purple',
          'red',
          'blue',
          'yellow',
          'pink',
          'green',
          'brown')
while True:
    x = random.randint(0,400)
    y = random.randint(0,400)

    for i, r in enumerate(range(150,181,5)):
        canvas.create_oval(x - r, y -r , x + r, y + r, outline=colors[i])
        canvas.update()
        time.sleep(0.05)