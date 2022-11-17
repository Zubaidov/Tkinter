from tkinter import *

root = Tk()
root.geometry('300x300')

mylabel1 = Label(root, text="Label 1").grid(row=0, column=0)
mylabel2 = Label(root, text="Label 2").grid(row=1, column=0)


root.mainloop()