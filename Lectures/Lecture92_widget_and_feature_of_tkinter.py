from tkinter import *  # can learn more at www.tkdocs.com


def say_hello_world():
    print("Hello World!!!")


mainWindow = Tk()
button = Button(mainWindow, text="Click Me", command=say_hello_world)
button.place(x=50, y=20)
mainWindow.mainloop()

# radio button
# combo box
# level
# check box
