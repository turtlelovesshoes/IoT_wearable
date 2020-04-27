from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learn")
#root.iconbitmap('c:/Library/Users/rmcguigan/Documents/my.ico')

my_img = ImageTk.PhotoImage(Image.open("aspen.png"))

button_quit= Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
