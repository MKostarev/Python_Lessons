#рисуем прямоугольники
import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
canvas.create_rectangle(20, 40, 200, 150)
canvas.create_rectangle(30, 50, 210, 160)
window.mainloop()
