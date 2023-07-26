import time
import tkinter
import random

window = tkinter.Tk()

canvas = tkinter.Canvas(window, width=1000, height=1000)
canvas.pack()
circles = []
colors = ['azure', 'aquamarine', 'blue',  'cyan', 'DarkGrey', 'firebrick1', 'gold', 'GreenYellow', 'grey35', 'HotPink', 'light slate blue', 'LightSeaGreen', 'navy', 'purple', 'RoyalBlue', 'SpringGreen', 'white', 'yellow', 'black']


def my_click(event):
    x = event.x
    y = event.y
    circle = {}
    circle["dx"] = random.randint(-10, 10)
    circle["dy"] = random.randint(-10, 10)

    r = len(circles)

    circle["id"] = canvas.create_oval(x - r, y - r, x + r, y + r, fill=random.choice(colors),outline=random.choice(colors))

    circles.append(circle)

canvas.bind('<Button-1>', my_click)

text_object = canvas.create_text(270, 30, text='количество объектов - {}'.format(len(circles)),fill=random.choice(colors),font=('arial',30 ))

while True:
    for circle in circles:
        x0, y0, x1, y1 = canvas.coords(circle['id'])
        if x0 < 0 or x1 > 1000:
            circle['dx'] = -circle['dx']
        if y0 < 0 or y1 > 1000:
            circle['dy'] = -circle['dy']

        canvas.move(circle['id'], circle['dx'], circle['dy'])
    canvas.itemconfig(text_object, text='количество объектов  - {}'.format(len(circles)))
    time.sleep(0.01)
    canvas.update()

window.mainloop()

