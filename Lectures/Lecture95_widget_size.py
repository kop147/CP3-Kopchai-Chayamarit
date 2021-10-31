from tkinter import *


def say_hello_world():
    print("Hello World!!!")


mainWindow = Tk()
button = Button(mainWindow, text="Click me 1", command=say_hello_world, width=20).grid(row=1, column=2)
button2 = Button(mainWindow, text="Click me 2", command=say_hello_world).grid(row=2, column=2)
button3 = Button(mainWindow, text="Click me 3", command=say_hello_world).grid(row=3, column=2)
label = Label(mainWindow, text="Hello World", width=20,).grid(row=2, column=1)  # add width
mainWindow.mainloop()
