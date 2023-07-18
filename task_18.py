#Разноцветные круги разных диматеров с общим центром
import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

for r in range(5, 96, 5):
    if r % 2 == 0:
        color = 'red'
    else:
        color = 'grey'
    canvas.create_oval(150-r, 100-r, 150+r, 100+r, outline=color)

window.mainloop()

collection = [25, "Иван", 103]
age, name, weight = collection
print(age, name, weight)
a = 1
b = 2
a, b = b, a


