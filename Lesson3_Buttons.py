from tkinter import *

root = Tk()
root.geometry('300x300')

def myClick():
    myLabel = Label(root, text="I have been clicked")
    myLabel.pack()

myButton = Button(root, text="Click me", pady=50, padx=50, command=myClick, fg="blue", bg="lightblue")
myButton.pack()

root.mainloop()