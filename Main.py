from tkinter import *
from volume1 import volume1Static

root = Tk()

C = Canvas(root, bg="gray55",height=200,width=800)

volume1Static(C, root)


C.pack()
mainloop()

