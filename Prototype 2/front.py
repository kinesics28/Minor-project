from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
root = Tk()
root.title("G meet assistant")
root.resizable(0,0)
bg = Image.open('background.png')
bg.thumbnail((900, 900))
width, height = bg.size
bg = ImageTk.PhotoImage(bg)


def new():
    if user_entry.get()=="":
        messagebox.showinfo("G Meet assistant", "Please enter the Username")
    elif password_entry.get()=="":
        messagebox.showinfo("G Meet assistant", "Please enter the Password")
    elif user_entry.get()=="" and password_entry.get()=="":
        messagebox.showinfo("G Meet assistant", "Please enter the Username and Password")
    else:
        os.system('python main.py')
        
        
canvas = Canvas(root, width=width, height=height, bd=0, highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')
label = Label(root, text="G-Meet assistant", font=("Ariel 25 bold"), bg='#5500FF', fg='white')
canvas.create_window(260, 40, anchor="nw", window=label)

mail_address = Label(root, text="Email ID:", font=("Ariel 18 bold"),bg='#5500FF',fg='white')
canvas.create_window(140, 130, anchor="nw", window=mail_address)

password = Label(root, text="Password:", font=("Ariel 18 bold"),bg='#5500FF',fg='white')
canvas.create_window(140, 210, anchor="nw", window=password)

#meetLink = Label(root, text="Meet Link:", font=("Ariel 18 bold"),bg='#5500FF',fg='white')
#canvas.create_window(140, 290, anchor="nw", window=meetLink)

user_entry = Entry(root, font=("Ariel 18 bold"))
user_entry.focus()

canvas.create_window(290, 130, anchor="nw", window=user_entry)
paswd=StringVar()
password_entry = Entry(root, textvar=paswd, font=("Ariel 18 bold"), show="*")
canvas.create_window(290, 210, anchor="nw", window=password_entry)
login = Button(root, text="Start!", font=("Ariel 22 bold"),
               width=8, bg="blue", fg='#FFC331', relief=FLAT, command=new)
canvas.create_window(270, 290, anchor="nw", window=login)
root.mainloop()