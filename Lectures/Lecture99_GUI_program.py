from tkinter import *
import math


def bmi_index(event):
    y = float(textBoxHeightInput.get())/100
    x = float(textboxWeightInput.get())
    result = (x/(math.pow(y, 2)))
    print(result)
    result_read = "x"
    if result < 18.5:
        result_read = "Eat More"
    elif result <= 22.90:
        result_read = "Normal"
    elif result <= 24.90:
        result_read = "Fat Level 1"
    elif result <= 30.00:
        result_read = "Fat Level 2"
    elif result > 30.00:
        result_read = "Fat Level 3"
    labelResult.configure(text=(x / (math.pow(y, 2))))
    labelResult2.configure(text=result_read)


mainWindow = Tk()
labelHeight = Label(mainWindow, text="Height (cm.)",).grid(row=0, column=0)
textBoxHeightInput = Entry(mainWindow,)
textBoxHeightInput.grid(row=0, column=1)
labelWeight = Label(mainWindow, text="weight (Kg.)").grid(row=1, column=0)
textboxWeightInput = Entry(mainWindow)
textboxWeightInput.grid(row=1, column=1)
calculateButton = Button(mainWindow, text="Calculate")
calculateButton.bind('<Button-1>', bmi_index)
calculateButton.grid(row=2, column=0)
labelResult = Label(mainWindow, text="result")
labelResult.grid(row=2, column=1)
labelResult2 = Label(mainWindow, text="result read", width=20, fg="red")
labelResult2.grid(row=3, columnspan=2)

mainWindow.mainloop()
