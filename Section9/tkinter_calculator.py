# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter

keys = [
    [("C", 1), ("CE", 1)],
    [("7", 1), ("8", 1), ("9", 1), ("+", 1)],
    [("4", 1), ("5", 1), ("6", 1), ("-", 1)],
    [("1", 1), ("2", 1), ("3", 1), ("*", 1)],
    [("0", 1), ("=", 2), ("/", 1)],
]

main_window = tkinter.Tk()
main_window.title("Calculator")
main_window.geometry("640x480-8-200")
main_window["padx"] = 8

result = tkinter.Entry(main_window)
result.grid(row=0, column=0, columnspan=4, sticky="nsew")

keypad_frame = tkinter.Frame(main_window)
keypad_frame.grid(row=1, column=0, sticky="nsew")

for i, key_row in enumerate(keys):
    column = 0
    for key in key_row:
        tkinter.Button(keypad_frame, text=key[0]).grid(
            row=i, column=column, sticky="ew", columnspan=key[1]
        )
        column += key[1]

main_window.update()
main_window.minsize(
    result.winfo_width() + keypad_frame.winfo_width(),
    result.winfo_height() + keypad_frame.winfo_height(),
)
main_window.maxsize(
    result.winfo_width() + keypad_frame.winfo_width() + 50,
    result.winfo_height() + keypad_frame.winfo_height() + 50,
)

main_window.mainloop()
