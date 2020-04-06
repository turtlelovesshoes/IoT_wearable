from Tkinter import *


root = Tk()

My_label = Label(root, text = "Hello World")
My_label2 = Label(root, text = "My name is Rachel")
#way to add space in line
#My_label3 = Label(root, text = "     ")

My_label.grid(row=0, column=0)
My_label2.grid(row=1, column=5)
#My_label3.grid(row=1, column=1)

First_widget = Label(root, text="These are my contacts!").grid(row=5, column=1)



root.mainloop()
