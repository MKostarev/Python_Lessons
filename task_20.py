#рисуем движущийся квадрат
import tkinter
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
x1 = 0
y1 = 0
x2 = 50
y2 = 50
delta = 2
rect = canvas.create_rectangle(x1, y1, x2, y2)
while True:
    pass
    x1 = x1 + delta
    x2 = x2 + delta
    canvas.update()
    time.sleep(0.01)
    canvas.coords(rect, x1, y1, x2, y2)
    if x1 > 200:
        delta = -delta
    elif x1 < 0:
        delta = -delta
window.mainloop()
