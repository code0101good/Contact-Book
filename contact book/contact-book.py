import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = Tk()

canvas = Canvas(root,width=400, height=600)
canvas.pack()
app_name = Label(root, text='Contact Register', font=('Arial',30))
canvas.create_window(200,50,window=app_name)

# LABEL
name = Label(root, text='Name')
Number = Label(root, text='Number')
canvas.create_window(200, 140, window=name)
canvas.create_window(200, 240, window=Number)

# INPUT
name_entry = Entry(root)
number_entry = Entry(root)
canvas.create_window(200, 160, window=name_entry)
canvas.create_window(200, 260, window=number_entry)

# BUTTON

def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    with open('contacts.txt', 'a') as f:
        f.write(f"Name: {name}\nNumber: {number}\n\n")
    messagebox.showinfo('Success, Contact added Successfull!y')

button = Button(root, text='Add Contact', command=add_contact)
canvas.create_window(200, 300, window=button)

root.mainloop()