import tkinter as tk
from tkinter import*
from tkinter.ttk import *
import random
window=tk.Tk()
window.title("Dice")

def roll_dice():
  p=label["text"]
  label["text"]= random.randint(1,6)
  

frame=tk.Frame(master=window ,relief=tk.RAISED)
butt=tk.Button(master =frame, text="Roll" ,height=2 , width=10 ,fg="white", bg="CornflowerBlue" , command = roll_dice)
butt.pack()
frame.pack()

frame2=tk.Frame(master=window)
label=tk.Label(master=frame2, text="4",)
label.pack()
frame2.pack()

window.mainloop()