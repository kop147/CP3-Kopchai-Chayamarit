from tkinter import *

main = Tk()

label1 = Label(main, text="Hello World", width=20, fg="red", bg="blue", font=("helvetica", 76), anchor=W).grid(row=1, column=1)
main.mainloop()  # anchor= is for text alignment where w = left  e = right
