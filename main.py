from tkinter import Tk, Label

root = Tk()

root.minsize(400, 400)
label1 = Label(root, text="Hello, world!")
label2 = Label(root, text="testing")


label1.pack()
label2.pack()
root.mainloop()