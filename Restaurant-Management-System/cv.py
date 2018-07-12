from tkinter import *
from tkinter import ttk

def test():
    name = userName.get()
    text = "Hello {0}! Pleased to meet you.".format(name)
    greeting.set(text)

window = Tk()

greeting = StringVar()
userName = StringVar()

name = Entry(window, textvariable=userName)
name.grid(column=1, row=1, sticky=NW)

button = Button(window, text="greeting", command=test)
button.grid(column=2, row=1, sticky=NW)

label = Label(window, textvariable=greeting)
label.grid(column=1, row=2, sticky=NW)



mainloop()