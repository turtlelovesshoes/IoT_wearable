#a script to play with tkinter for first time and to use for reference
#while building the interface
# Please continue from https://realpython.com/python-gui-tkinter/ 

import tkinter as tk

 window = tk.Tk()

greeting = tk.Label(text="python rocks!")
greeting.pack()

button = tk.Button(
     text="Click me!",
     width=25,
     height=5,
     bg="blue",
    fg="yellow",
 )
button.pack()
entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()


window.mainloop()
