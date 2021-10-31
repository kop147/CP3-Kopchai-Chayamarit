from tkinter import *


def left_click_button(event):
    print("Left Click")


def right_click_button(event):
    print("Right Click")


def double_click(event):
    print("Double Click!!")


main = Tk()
button = Button(main, text="My button!!!")
button.pack()  # .bind for binding event with function
button.bind('<Button-1>', left_click_button)   # <Button-1> = left click  <Button-3> = middle click
button.bind('<Button-2>', right_click_button)  # <Button-2> = right click
button.bind('<Double-1>', double_click)  # <Double-1> = left Double click
main.mainloop()

