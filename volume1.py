from tkinter import *

root = Tk()
C = Canvas(root, bg="gray55",height=200,width=1000)

def create_circle(x, y, r, o, w, C): #center coordinates, radius, outline Color, width
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return C.create_oval(x0, y0, x1, y1,outline= o, width= w )

def volume1Static():
   frame = C.create_rectangle(10,10,990,190,outline ="black",fill ="gray15",width = 2)
   volumecontrollring = create_circle(900,85,40, "black", 6, C)
   displaybg = C.create_rectangle(50,30,800,140, fill='#4a1500')
   displayoutline =  C.create_rectangle(50,30,800,140,outline ='black', width = 4)
   displayVUr = C.create_text(80, 66, text="L", fill="blue", font=("Arial", 16))
   displayVUl = C.create_text(80, 102, text="R", fill="red", font=("Arial", 16))

#def VUdisplay(LevelL,LevelR):

    


volume1Static()
C.pack()
mainloop()