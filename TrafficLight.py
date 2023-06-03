import os
from tkinter import *
from time import sleep

root = Tk()
root.title('Traffic Light')

label = Label(root)
label.pack()

image = PhotoImage(file="TrafficLight/img/idle.png")

label.configure(image=image)

image_paths = [ "red.png", "green.png", "yellow.png" ]
i = 0

def update_signal():
    global image
    global i
    
    files = os.listdir("TrafficLight/img")
    
    new_image = PhotoImage(file=f"TrafficLight/img/{image_paths[i]}")
    
    label.configure(image=new_image)
    image = new_image

    if i == 0:
        sleep(0.0001)
    if i == 1:
        sleep(4)
    if i == 2:
        sleep(5)

    i += 1
    if i > 2:
        i = 0
    
    root.after(1000, update_signal)

root.after(1000, update_signal)
root.mainloop()
