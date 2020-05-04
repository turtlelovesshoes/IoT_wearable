from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Viewing some images")

my_img1 = ImageTk.PhotoImage(Image.open("images_viewer/terminal_rasp.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images_viewer/button_light.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images_viewer/led_potentiometer.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images_viewer/joystick.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images_viewer/button_motor.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward():
	global my_label
	global forward_button
	global back_buton

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	forward_button = Button(root, text = ">>", command=lambda: forward(image_number+1))
	back_button = Button(root, text="<<", command=lambda: back(image_number+1))
	if image_number == 5:
		forward_button = Button(root, text=">>", state=DISABLED)
	my_label.grid(row=0, column=0, columnspan=3)
	back_buton.grid(row=1, column=0)
	button_exit.grid(row=1, column=1)
	forward_button.grid(row=1, column=2)
	root.pack()

	
def back():
	global my_label
	global forward_button
	global back_buton

	my_label.grid_forget()
	my_label = Label(image = image_list[image_number-1])
	forward_button = Button(root, text = ">>", command=lambda: forward(image_number+1))
	back_button = Button(root, text="<<", command=lambda: back(image_number+1))
	if image_number == 1:
		back_button = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	back_buton.grid(row=1, column=0)
	button_exit.grid(row=1, column=1)
	forward_button.grid(row=1, column=2)
	root.pack()
	



back_buton = Button(root, text="<<", command=back)
forward_button = Button(root, text=">>", command=lambda: forward(2))
button_exit= Button(root, text = "exit program", command=root.quit())

back_buton.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
forward_button.grid(row=1, column=2)

root.mainloop()
