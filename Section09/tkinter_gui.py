import os
import tkinter
from unittest import result

main_window = tkinter.Tk()

main_window.title("Grid Demo")
main_window.geometry("640x480+600+300")
main_window["padx"] = 8

label = tkinter.Label(main_window, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

# Configure the columns and rows
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=3)
main_window.columnconfigure(3, weight=3)
main_window.columnconfigure(4, weight=3)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=10)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=3)
main_window.rowconfigure(4, weight=3)

# WIDGET: Listbox with system32 directory files
file_list = tkinter.Listbox(main_window)
file_list.grid(row=1, column=0, sticky="nsew", rowspan=2)
file_list.config(border=2, relief="sunken")
for zone in os.listdir("/Windows/System32"):
    file_list.insert(tkinter.END, zone)

# WIDGET: Listbox Scrollbar
list_scroll = tkinter.Scrollbar(
    main_window, orient=tkinter.VERTICAL, command=file_list.yview
)
list_scroll.grid(row=1, column=1, sticky="nsw", rowspan=2)
file_list["yscrollcommand"] = list_scroll.set

# WIDGET: Radio buttons
option_frame = tkinter.LabelFrame(main_window, text="File Details")
option_frame.grid(row=1, column=2, sticky="ne")
rb_value = tkinter.IntVar()  # Variable to store the selected radio button
rb_value.set(2)  # Default value
radio_1 = tkinter.Radiobutton(option_frame, text="Filename", value=1, variable=rb_value)
radio_2 = tkinter.Radiobutton(option_frame, text="Path", value=2, variable=rb_value)
radio_3 = tkinter.Radiobutton(
    option_frame, text="Timestamp", value=3, variable=rb_value
)
radio_1.grid(row=0, column=0, sticky="w")
radio_2.grid(row=1, column=0, sticky="w")
radio_3.grid(row=2, column=0, sticky="w")

# WIDGET: Result field
result_label = tkinter.Label(main_window, text="Result")
result_label.grid(row=2, column=2, sticky="nw")
result_field = tkinter.Entry(main_window)
result_field.grid(row=2, column=2, sticky="sw")

# WIDGET: Time spinners
time_frame = tkinter.LabelFrame(main_window, text="Time")
time_frame.grid(row=3, column=0, sticky="new")
hour_spinner = tkinter.Spinbox(
    time_frame, width=2, values=tuple(str(x) for x in range(24))
)
minute_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
second_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=":").grid(row=0, column=1)
minute_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=":").grid(row=0, column=3)
second_spinner.grid(row=0, column=4)
time_frame["padx"] = 36

# WIDGET: Date spinners
date_frame = tkinter.Frame(main_window)
date_frame.grid(row=4, column=0, sticky="new")
day_label = tkinter.Label(date_frame, text="Day")
month_label = tkinter.Label(date_frame, text="Month")
year_label = tkinter.Label(date_frame, text="Year")
day_label.grid(row=0, column=0, sticky="w")
month_label.grid(row=0, column=1, sticky="w")
year_label.grid(row=0, column=2, sticky="w")
day_spin = tkinter.Spinbox(date_frame, width=5, from_=1, to=31)
month_spin = tkinter.Spinbox(
    date_frame,
    width=5,
    values=(
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ),
)
year_spin = tkinter.Spinbox(date_frame, width=5, from_=2000, to=2099)
day_spin.grid(row=1, column=0)
month_spin.grid(row=1, column=1)
year_spin.grid(row=1, column=2)

# Buttons
ok_button = tkinter.Button(main_window, text="OK")
cancel_button = tkinter.Button(main_window, text="Cancel", command=main_window.quit)
ok_button.grid(row=4, column=3, sticky="e")
cancel_button.grid(row=4, column=4, sticky="w")

# Main loop
main_window.mainloop()
