from tkinter import *

root = Tk()
root.geometry("300x300")

entr = Entry(root, borderwidth=5)
entr.pack()

def myClick():
    myLabel = Label(root, text=entr.get())
    myLabel.pack()

myButton = Button(root, text="See More", bg="lightblue", fg="black", command=myClick).pack()



root.mainloop()