import tkinter

main_window = tkinter.Tk()

main_window.title("Title Hello World")
main_window.geometry("640x480+600+300")

label = tkinter.Label(main_window, text="Label Hello World")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(main_window)
leftFrame.grid(row=1, column=0, sticky="s")

canvas = tkinter.Canvas(main_window, relief="raised", borderwidth=1)
#! It can fill the whole window but needs to set expand = True to make it work
# canvas.pack(side="left", fill=tkinter.BOTH, expand=True)
canvas.grid(row=1, column=1)

rightFrame = tkinter.Frame(main_window)
rightFrame.grid(row=1, column=2, sticky="n")

button1 = tkinter.Button(leftFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# Configure the columns
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)

# Configure the rows
leftFrame.config(relief="sunken", borderwidth=1)
leftFrame.grid(sticky="ns")
rightFrame.config(relief="sunken", borderwidth=1)
rightFrame.grid(sticky="new")

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky="ew")

main_window.mainloop()
