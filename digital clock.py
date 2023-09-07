# module importing
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

root = Tk()
root.title("Rohit's Clockitty")

# function to display date and time

def time():
    string = strftime('%H:%M:%S: %p')
    label.config(text=string)
    label.after(1000, time)

# Styling the label widget for the clock output
label = Label(root , font=("ds-digital", 200), background="black", foreground="Purple")
# placing the clock at center
label.pack(anchor='center')
time()
mainloop()