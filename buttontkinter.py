from Tkinter import *


root = Tk()

e = Entry(root, width=50, fg="blue", borderwidth=5)
e.pack()

name_label = Label(root, text = "First Name:").pack()
name_e = Entry(root, width=50, fg="blue", borderwidth=5)
name_e.pack()
last_label= Label(root, text = "Last Name:").pack()
last_e = Entry(root, width=50, fg="blue", borderwidth=5)
last_e.pack()
number_label = Label(root, text = "Phone Number").pack()
number = Entry(root, width=50, fg="blue", borderwidth=5)
number.pack()


def get_entry():
   myLabel = Label(root, text=e.get())
   myLabel.pack()

def myClick():
   myLabel = Label(root, text="Look! You clicked the button")
   myLabel.pack()

myButton = Button(root, text="Button",padx=50,pady=50,command=get_entry,bg="blue")
myButton.pack()

root.mainloop()
