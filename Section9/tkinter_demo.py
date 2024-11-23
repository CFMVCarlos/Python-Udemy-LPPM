import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)
tkinter._test()

main_window = tkinter.Tk()

main_window.title("Title Hello World")
main_window.geometry("640x480+600+300")

main_window.mainloop()
