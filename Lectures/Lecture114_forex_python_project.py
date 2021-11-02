# Bitcoin short trend
import datetime
import tkinter.ttk

from forex_python.bitcoin import BtcConverter
from datetime import date
from tkinter import *


def day(choose_day, no_of_day):
    return choose_day - (datetime.timedelta(days=no_of_day))


def trend(data):
    test_function_x = len(data) - 1
    length_of_data = len(data) - 1
    if data[0] > data[length_of_data]:
        up_down_indicator = "UP!!"
    else:
        up_down_indicator = "DOWN!!"

    type_indicator = ""

    while data[test_function_x] > data[test_function_x - 1]:
        if test_function_x == 1:
            type_indicator = "BEARISH"
            break
        else:
            test_function_x -= 1

    while data[test_function_x] < data[test_function_x - 1]:
        if test_function_x == 1:
            type_indicator = "BULLISH"
            break
        else:
            test_function_x -= 1
    if type_indicator == "":
        type_indicator = "Sideways"

    return type_indicator, up_down_indicator


def get_values():
    from_date = date(int(from_year_combobox.get()), int(from_month_combobox.get()), int(from_day_combobox.get()))
    to_date = date(int(to_year_combobox.get()), int(to_month_combobox.get()), int(to_day_combobox.get()))
    number_of_day = to_date - from_date
    day_count = number_of_day.days
    future_check = (datetime.date.today() - to_date).days

    if day_count <= 0:
        label_result.configure(text="error please enter date again!!!")
    elif future_check <= 0:
        label_result.configure(text="error please enter date again!!!")
    else:
        list_of_day = []
        for i in range(day_count):
            list_of_day.append(day(to_date, i))
        list_of_price = []
        b = BtcConverter()
        for i in list_of_day:
            list_of_price.append(b.get_previous_price("THB", i))
        result = (trend(list_of_price))
        print(result[0])
        print(result[1])
        if result[1] == "UP!!":
            label_result.configure(text="The trend is %s %s" % (result[0], result[1]), fg="green")
        else:
            label_result.configure(text="The trend is %s %s" % (result[0], result[1]), fg="red")


day_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
year_list = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]


input_day = ""
main_window = Tk()

main_window.title("Bitcoin Trend")

from_label = Label(main_window, text="FROM").grid(row=2, column=0, rowspan=2, sticky='ns')

Label_box1 = Label(main_window, text="date").grid(row=2, column=2)
Label_box2 = Label(main_window, text="month").grid(row=2, column=3)
Label_box3 = Label(main_window, text="year").grid(row=2, column=4)

from_day_combobox = tkinter.ttk.Combobox(main_window, values=day_list, state='readonly')
from_day_combobox.set("Pick a day")
from_day_combobox.grid(row=3, column=2)

from_month_combobox = tkinter.ttk.Combobox(main_window, values=month_list, state='readonly')
from_month_combobox.set("Pick a month")
from_month_combobox.grid(row=3, column=3)

from_year_combobox = tkinter.ttk.Combobox(main_window, values=year_list, state='readonly')
from_year_combobox.set("Pick a year")
from_year_combobox.grid(row=3, column=4)

to_label = Label(main_window, text="TO").grid(row=4, column=0, rowspan=2, sticky='ns')

Label_box4 = Label(main_window, text="date").grid(row=4, column=2)
Label_box5 = Label(main_window, text="month").grid(row=4, column=3)
Label_box6 = Label(main_window, text="year").grid(row=4, column=4)

to_day_combobox = tkinter.ttk.Combobox(main_window, values=day_list, state='readonly')
to_day_combobox.set("Pick a day")
to_day_combobox.grid(row=5, column=2)

to_month_combobox = tkinter.ttk.Combobox(main_window, values=month_list, state='readonly')
to_month_combobox.set("Pick a month")
to_month_combobox.grid(row=5, column=3)

to_year_combobox = tkinter.ttk.Combobox(main_window, values=year_list, state='readonly')
to_year_combobox.set("Pick a year")
to_year_combobox.grid(row=5, column=4)

calculate_button = Button(main_window, text="Calculate The Trend", command=get_values)
calculate_button.grid(row=6, columnspan=5, sticky='ew')

label_result = Label(main_window, text="Currently trend is", font=("Helvetica", 36))
label_result.grid(row=7, columnspan=5, rowspan=3, sticky='nsew')
main_window.mainloop()
