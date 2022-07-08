from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
window = Tk()
window.geometry('300x200')
window.title("Welcome to G-meet Assistant")


image_0 = Image.open("2.png")
bck_end = ImageTk.PhotoImage(image_0)
lbl = Label(window,image=bck_end)
lbl.place(x=0, y=0)

a = Label(window ,text = "Meet Link").grid(row = 0,column = 0)
b = Label(window ,text = "Email Id").grid(row = 1,column = 0)
c = Label(window ,text = "Password").grid(row = 2,column = 0)
a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)
window.mainloop()