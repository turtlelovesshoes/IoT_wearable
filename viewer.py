from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Viewing some images")

my_img = ImageTk.PhotoImage(Image.open("images/aspen.jpeg"))
my_label = Label(image=my_img)
my_label.pack()


root.mainloop()
