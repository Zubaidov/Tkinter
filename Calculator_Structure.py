from tkinter import *

root = Tk()
root.title("Simple Calculater")

entry = Entry(root, width=55, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3)

def button_click(number):
    entry.insert(0, number)

Button_1 = Button(root, text="1", padx="40px", pady="20px", command= lambda: button_click(1)).grid(row=3, column=0)
Button_2 = Button(root, text="2", padx="40px", pady="20px", command= lambda: button_click(2)).grid(row=3, column=1)
Button_3 = Button(root, text="3", padx="40px", pady="20px", command= lambda: button_click(3)).grid(row=3, column=2)
Button_4 = Button(root, text="4", padx="40px", pady="20px", command= lambda: button_click(4)).grid(row=2, column=0)
Button_5 = Button(root, text="5", padx="40px", pady="20px", command= lambda: button_click(5)).grid(row=2, column=1)
Button_6 = Button(root, text="6", padx="40px", pady="20px", command= lambda: button_click(6)).grid(row=2, column=2)
Button_7 = Button(root, text="7", padx="40px", pady="20px", command= lambda: button_click(7)).grid(row=1, column=0)
Button_8 = Button(root, text="8", padx="40px", pady="20px", command= lambda: button_click(8)).grid(row=1, column=1)
Button_9 = Button(root, text="9", padx="40px", pady="20px", command= lambda: button_click(9)).grid(row=1, column=2)
Button_0 = Button(root, text="0", padx="40px", pady="20px", command= lambda: button_click(0)).grid(row=4, column=0)
Button_add = Button(root, text="+", padx="39px", pady="20px", command= lambda: button_click()).grid(row=5, column=0)
Button_equal = Button(root, text="=", padx="86px", pady="20px", command= lambda: button_click()).grid(row=5, column=1, columnspan=2)
Button_clear = Button(root, text="Clear", padx="79px", pady="20px", command= lambda: button_click()).grid(row=4, column=1, columnspan=2)


root.mainloop()