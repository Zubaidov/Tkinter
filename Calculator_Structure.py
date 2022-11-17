from tkinter import *

root = Tk()

myEntry = Entry(root, borderwidth=5)
myEntry.grid(row=0, column=0, columnspan=3)


myButton7 = Button(root, text="7", padx="15px", pady="15px")
myButton7.grid(row=1, column=0)

myButton8 = Button(root, text="8", padx="15px", pady="15px")
myButton8.grid(row=1, column=1)

myButton9 = Button(root, text="9", padx="15px", pady="15px")
myButton9.grid(row=1, column=2)

myButton4 = Button(root, text="4", padx="15px", pady="15px")
myButton4.grid(row=2, column=0)

myButton5 = Button(root, text="5", padx="15px", pady="15px")
myButton5.grid(row=2, column=1)

myButton6 = Button(root, text="6", padx="15px", pady="15px")
myButton6.grid(row=2, column=2)

myButton1 = Button(root, text="1", padx="15px", pady="15px")
myButton1.grid(row=3, column=0)

myButton2 = Button(root, text="2", padx="15px", pady="15px")
myButton2.grid(row=3, column=1)

myButton3 = Button(root, text="3", padx="15px", pady="15px")
myButton3.grid(row=3, column=2)

root.mainloop()