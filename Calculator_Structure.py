from tkinter import *

root = Tk()

Entry = Entry(root, width=35, borderwidth=5)
Entry.grid(row=0, column=0, columnspan=3)
result = Entry.get()

def button_add():
    print(result)

Button_1 = Button(root, text="1", padx="40px", pady="20px", command=button_add).grid(row=3, column=0)
Button_2 = Button(root, text="2", padx="40px", pady="20px", command=button_add).grid(row=3, column=1)
Button_3 = Button(root, text="3", padx="40px", pady="20px", command=button_add).grid(row=3, column=2)
Button_4 = Button(root, text="4", padx="40px", pady="20px", command=button_add).grid(row=2, column=0)
Button_5 = Button(root, text="5", padx="40px", pady="20px", command=button_add).grid(row=2, column=1)
Button_6 = Button(root, text="6", padx="40px", pady="20px", command=button_add).grid(row=2, column=2)
Button_7 = Button(root, text="7", padx="40px", pady="20px", command=button_add).grid(row=1, column=0)
Button_8 = Button(root, text="8", padx="40px", pady="20px", command=button_add).grid(row=1, column=1)
Button_9 = Button(root, text="9", padx="40px", pady="20px", command=button_add).grid(row=1, column=2)
Button_0 = Button(root, text="0", padx="40px", pady="20px", command=button_add).grid(row=4, column=0)
Button_add = Button(root, text="+", padx="39px", pady="20px", command=button_add).grid(row=5, column=0)
Button_equal = Button(root, text="=", padx="86px", pady="20px", command=button_add).grid(row=5, column=1, columnspan=2)
Button_clear = Button(root, text="Clear", padx="79px", pady="20px", command=button_add).grid(row=4, column=1, columnspan=2)


root.mainloop()