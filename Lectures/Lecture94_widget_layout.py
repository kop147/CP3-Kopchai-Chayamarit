import tkinter


def say_hello_world():
    print("Hello World!!!")

''' Example 1
mainWindow = tkinter.Tk()
button = tkinter.Button(mainWindow, text="Click Me", command=say_hello_world)
button.place(x=50, y=20)  # origin start from top left conner
button2 = tkinter.Button(mainWindow, text="Click Me2", command=say_hello_world)
button2.place(x=150, y=120)
mainWindow.mainloop() '''

# ex2
mainWindow = tkinter.Tk()
button = tkinter.Button(mainWindow, text="Click Me", command=say_hello_world).grid(row=0, column=0)
button2 = tkinter.Button(mainWindow, text="Click Me2", command=say_hello_world).grid(row=1, column=1)
button3 = tkinter.Button(mainWindow, text="Click Me3", command=say_hello_world).grid(row=1, column=4)
mainWindow.mainloop()

