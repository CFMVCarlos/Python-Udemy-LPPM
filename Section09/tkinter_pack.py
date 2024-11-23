import tkinter

main_window = tkinter.Tk()

main_window.title("Title Hello World")
main_window.geometry("640x480+600+300")

label = tkinter.Label(main_window, text="Label Hello World")
label.pack(side="top")

leftFrame = tkinter.Frame(main_window)
leftFrame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(main_window, relief="raised", borderwidth=1)
#! It can fill the whole window but needs to set expand = True to make it work
# canvas.pack(side="left", fill=tkinter.BOTH, expand=True)
canvas.pack(side="left", anchor="n")

rightFrame = tkinter.Frame(main_window)
rightFrame.pack(side="right", anchor="n", expand=True)

button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")

button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")

main_window.mainloop()
