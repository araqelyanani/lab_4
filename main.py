import tkinter as tk
from tkinter.messagebox import showinfo, showerror
import random
import time


def open_error():
    showerror(title="Error", message='Lenght is not equal to 5')


def open_info():
    showinfo(title="Result", message=g_key(int(str(entry.get()), 16)))


def g_key(x):
    a = str(x)
    cif = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    k = str(str(a[0]) + rand() + '-' + str(a[1]) + rand() + '-' + str(a[2]) + rand() + '-' + str(a[-2:]))
    return k


def rand():
    cif = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return str(random.choice(cif)) + str(random.choice(cif)) + str(random.choice(cif)) + str(random.choice(cif))


def f():
    if len(str(entry.get())) != 5:
        return open_error()
    else:
        return open_info()


def motion():
    c.move(rec, 1, 0)
    c.after(50, motion)


window = tk.Tk()
window.title("generatorX26")
window.geometry('360x240')
bg = tk.PhotoImage(file='brawlstars.png')

w = tk.Label(window, image=bg)
w.place(x=-2, y=0)

label = tk.Label(text="Enter a number in HEX length of 5 characters",
                 fg="white", bg="light salmon", font=('Courier', 8))
label.place(x=25, y=60)

entry = tk.Entry(fg="salmon4", width=20)
entry.place(x=120, y=90)

button = tk.Button(text="Generate", width=8, height=1, fg="salmon4", font=('Courier', 8), command=f)
button.place(x=270, y=200)


c = tk.Canvas(window, width=120, height=10)
c.place(x=120, y=115)
rec = c.create_rectangle(0, 0, 120, 60, outline="light salmon", fill="light salmon")

motion()

window.mainloop()


